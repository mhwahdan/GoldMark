(function ($) {
    "use strict";

    $(document).ready(function () {

        /**
         * RVR Booking Form AJAX validation and submission
         * Validation Plugin : https://jqueryvalidation.org/
         * Form Ajax Plugin : http://www.malsup.com/jquery/form/
         */

        if (jQuery().validate && jQuery().ajaxSubmit) {

            $(".rvr-booking-form").each(function(){
				var $form = $(this);

				var submitButton = $form.find('.rvr-booking-button'),
                ajaxLoader = $form.find('.rvr-ajax-loader'),
                messageContainer = $form.find('.rvr-message-container'),
                errorContainer = $form.find(".rvr-error-container");

				var formOptions = {
					beforeSubmit: function () {
						submitButton.attr('disabled', 'disabled');
						ajaxLoader.css('display','block');
						ajaxLoader.fadeIn('fast');
						messageContainer.fadeOut('fast');
						errorContainer.fadeOut('fast');
					},
					success: function (ajax_response, statusText, xhr, $form) {
						var response = $.parseJSON(ajax_response);
						ajaxLoader.fadeOut('fast');
						submitButton.removeAttr('disabled');
						
						if ( response.checkout_url ) {
							window.location.href = response.checkout_url;
						} if (response.success) {
							$form.resetForm();
							$form.children('.booking-cost').slideUp('fast');

							messageContainer.html(response.message).fadeIn('fast');

							setTimeout(function () {
								messageContainer.fadeOut('fast').empty();
							},5000);
							
							// call reset function if it exists
							if (typeof inspiryResetReCAPTCHA == 'function') {
								inspiryResetReCAPTCHA();
							}

						} else {
							errorContainer.html(response.message).fadeIn('fast');
						}
					}
            };

			$form.validate({
				submitHandler: function (form) {
						const bookingCost = {
							data: {
								price_staying_nights: $form.find('.staying-nights-field').children('.cost-value').data('stayingNights'),
								govt_tax: $form.find('.govt-tax-field').children('.cost-value').data('govtTax'),
								services_charges: $form.find('.services-charges-field').children('.cost-value').data('serviceCharges'),
								staying_nights: $form.find('.staying-nights-count-field').children('.cost-value').data('staying-nights'),
								total_price: $form.find('.total-price-field').children('.cost-value').data('total'),
							}
						};

						$.extend(formOptions, bookingCost);
						$(form).ajaxSubmit(formOptions);
					}
				});
			});

        }

        /**
         * Search Form Datepicker (only modern)
         */
        var dates = $("#rvr-check-in-search, #rvr-check-out-search").datepicker({
            minDate: new Date(),
            dateFormat: 'yy-mm-dd',
            onSelect: function (selectedDate) {
                var option = this.id == "rvr-check-in-search" ? "minDate" : "maxDate",
                    instance = $(this).data("datepicker"),
                    date = $.datepicker.parseDate(instance.settings.dateFormat || $.datepicker._defaults.dateFormat, selectedDate, instance.settings);

					if( 'minDate' === option ) {
						date.setDate(date.getDate() + 1);
					} else {
						date.setDate(date.getDate() - 1);
					}

                	dates.not(this).datepicker("option", option, date );
			},
            beforeShow: function () {
            	$(this).parents('.rh_mod_text_field').addClass('rh_mod_text_field_focused');
            } ,
            onClose: function () {
                if (!$(this).val()) {
                    $(this).parents('.rh_mod_text_field').removeClass('rh_mod_text_field_focused');
                    $( this ).datepicker( "refresh" );
                }
            }

        });

        /**
         * Search/Booking Forms Datepicker
         */
		$(".rvr-booking-form").each(function(){
			var dateToday = new Date();
			var $form = $(this);
			const checkIn = $form.find('.rvr-check-in');
			const checkOut = $form.find('.rvr-check-out');
			const costTable = $form.children('.booking-cost');

			const pricePerNight = $form.find('.price-per-night').val();
			const serviceCharges = parseInt($form.find('.service-charges').val());
			const govtTax = parseInt($form.find('.govt-charges').val());

			var dates = $form.find(".rvr-check-in, .rvr-check-out").datepicker({
				minDate: dateToday,
				dateFormat: 'yy-mm-dd',
				beforeShowDay: function (date) {

					const availability_calendar = $('#property-availability');
					if (availability_calendar.length) {
						var reserved_dates = availability_calendar.data('dates');

						if ('' != reserved_dates) {
							reserved_dates = reserved_dates.split(",");
						} else {
							reserved_dates = '';
						}

						var string = jQuery.datepicker.formatDate('yy-mm-dd', date);

						var today = new Date();

						if (date > today || today) {

							if (reserved_dates.indexOf(string) != -1) {
								return [false, 'ui-state-reserved'];
							} else {
								return [true, '']
							}
						} else {
							return [true, '']
						}

					} else {
						return [true, '']
					}

				},
				onSelect: function (selectedDate) {
					var option = $(this).hasClass('rvr-check-in') ? "minDate" : "maxDate",
						instance = $(this).data("datepicker"),
						date = $.datepicker.parseDate(instance.settings.dateFormat || $.datepicker._defaults.dateFormat, selectedDate, instance.settings);
						
						if( 'minDate' === option ) {
							date.setDate(date.getDate() + 1);
						} else {
							date.setDate(date.getDate() - 1);
						}

						dates.not(this).datepicker("option", option, date);

					if (!pricePerNight) {
						return;
					}

					var startDate = checkIn.datepicker('getDate');
					var endDate = checkOut.datepicker('getDate');

					if (startDate && endDate) {

						const days = ((endDate - startDate) === 0) ? 1 : (endDate - startDate) / 1000 / 60 / 60 / 24;

						var costStayingNights = pricePerNight * days;
						var costServiceCharges = (costStayingNights * serviceCharges) / 100;
						var costGovtTax = (costStayingNights * govtTax) / 100;

						costServiceCharges = (isNaN(costServiceCharges)) ? 0 : costServiceCharges;
						costGovtTax = (isNaN(costGovtTax)) ? 0 : costGovtTax;

						var costTotal = costStayingNights + costServiceCharges + costGovtTax;

						$form.ajaxSubmit(
							{
								data: {
									action: 'rvr_format_prices',
									prices: {
										costStayingNights,
										costServiceCharges,
										costGovtTax,
										costTotal
									}
								},
								success: function (response) {
									var response_json = $.parseJSON(response);
									var prices = response_json.formatted_prices;

									prices.costStayingNights = (prices.costStayingNights == false) ? costStayingNights : prices.costStayingNights;
									prices.costServiceCharges = (prices.costServiceCharges == false) ? costServiceCharges : prices.costServiceCharges;
									prices.costGovtTax = (prices.costGovtTax == false) ? costGovtTax : prices.costGovtTax;
									prices.costTotal = (prices.costTotal == false) ? costTotal : prices.costTotal;

									const snField = $form.find('.staying-nights-count-field').children('.cost-value');
									const psnField = $form.find('.staying-nights-field').children('.cost-value');
									const gtField = $form.find('.govt-tax-field').children('.cost-value');
									const scField = $form.find('.services-charges-field').children('.cost-value');
									const tpField = $form.find('.total-price-field').children('.cost-value');

									snField.text(Math.round(days));
									psnField.text(prices.costStayingNights);
									scField.text(prices.costServiceCharges);
									gtField.text(prices.costGovtTax);
									tpField.text(prices.costTotal);

									snField.data('staying-nights', Math.round(days));
									psnField.data('staying-nights', Math.round(costStayingNights));
									gtField.data('govt-tax', Math.round(costGovtTax));
									scField.data('service-charges', Math.round(costServiceCharges));
									tpField.data('total', Math.round(costTotal));
								}
							}
						);

						costTable.slideDown('fast');
					}
					$(this).blur(); // To remove form validation JS error when a date is selected.
				},
			});
		});

        /**
         * Property Availability Calendar
         */
        const availability_calendar = $('#property-availability');
        if (availability_calendar.length) {
            var reserved_dates = availability_calendar.data('dates');

            if ('' !== reserved_dates) {
                reserved_dates = reserved_dates.split(",");

				let calendar_options = {
                    num_next_month: 1,
                    unavailable: reserved_dates,
                    minDate: 0,
					day_first: 1,
                };

				if('undefined' !== typeof(availability_calendar_data)) {
					calendar_options.day_name = availability_calendar_data.day_name;
					calendar_options.month_name = availability_calendar_data.month_name;
				}
				
                availability_calendar.calendar(calendar_options);
            } 
        }

    });

})(jQuery);