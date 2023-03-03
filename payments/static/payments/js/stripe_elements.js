

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey)
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card');
card.mount('#card-element')

// Handle validation errors on the card element
card.AddEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class=icon role=alert>
                <i class=fas fa fa-times></i>
            </span>
            <span>${event.error.message}</span>
            `
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);

    var safeInfo = Boolean($('#id-safe-info').attr('checked'));
    var token = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': client_secret,
        'save_info': save_info,
    };
    var url = '/payments/safe_payment_data/';
    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                payment_info: {
                    fist_name: $.trim(form.first_name.value),
                    last_name: $.trim(form.last_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        street_address: $.trim(form.street_address.value),
                        house_number: $.trim(form.house_number.value),
                        postcode: $.trim(form.postcode.value),
                        city: $.trim(form.city.value),
                        county: $.trim(form.county.value),
                        country: $.trim(form.country.value),

                    }
                }
            },
            shipping_info: {
                fist_name: $.trim(form.first_name.value),
                last_name: $.trim(form.last_name.value),
                phone: $.trim(form.phone_number.value),
                email: $.trim(form.email.value),
                address: {
                    street_address: $.trim(form.street_address.value),
                    house_number: $.trim(form.house_number.value),
                    postcode: $.trim(form.postcode.value),
                    city: $.trim(form.city.value),
                    county: $.trim(form.county.value),
                    country: $.trim(form.country.value),
                },
            },

        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function() {
        location.reload();
    })
});