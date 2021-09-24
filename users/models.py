from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.apps import apps
from django.contrib import auth


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, firstname=None, lastname=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        if not firstname:
            raise ValueError('First name must be set')
        if not lastname:
            raise ValueError('Last name must be set')
        if not username:
            raise ValueError('user name must be set')
        email = self.normalize_email(email=email)
        model = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        username = model.normalize_username(username)
        user = self.model(username=username ,firstname=firstname, lastname=lastname, email=email, **extra_fields)
        user.password = make_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_user(self, email, username, firstname=None, lastname=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email=email, username=username, firstname=firstname, lastname=lastname,
                                 password=password, **extra_fields)

    def create_superuser(self, email, username, firstname=None, lastname=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email=email, username=username, firstname=firstname, lastname=lastname,
                                 password=password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument.'
                )
        elif not isinstance(backend, str):
            raise TypeError(
                'backend must be a dotted import path string (got %r).'
                % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, 'with_perm'):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, verbose_name="user name", unique=True)
    firstname = models.CharField(max_length=50, verbose_name="first name")
    lastname = models.CharField(max_length=50, verbose_name="last name")
    email = models.EmailField(max_length=100, verbose_name="email address", unique=True)
    phone = models.CharField(max_length=11, verbose_name="primary phone number",
                             blank=True, null=True)
    image = models.ImageField(upload_to='theBank/users/profile pictures/', verbose_name='Profile picture',
                              blank=True, null=True)
    date_joined = models.DateTimeField(verbose_name='date joined', default=timezone.now)
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = [
        'firstname',
        'lastname',
        'email'
    ]

    class Meta(AbstractUser.Meta):
        verbose_name = 'user'
        verbose_name_plural = 'users'
        swappable = 'AUTH_USER_MODEL'

    is_staff = models.BooleanField(
        verbose_name='staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.'
    )

    is_active = models.BooleanField(
        verbose_name='active status',
        default=True,
        help_text='Designates whether this user should be treated as active. '
    )

    is_admin = models.BooleanField(
        verbose_name='admin status',
        default=True,
        help_text='Designates whether this user should be treated as admin. '
    )

    objects = UserManager()

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    username_validator = UnicodeUsernameValidator()

