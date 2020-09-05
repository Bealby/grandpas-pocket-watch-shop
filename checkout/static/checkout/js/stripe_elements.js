/*
 *  Core logic/payment flow for this comes from Stripe documentations:
 *  https://stripe.com/docs/payments/accept-a-payment
 *  with minor modification and additions
 */

let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: 'rgb(170, 183, 196)'
        }
    },
    /*changr colors????*/
    invalid: {
        color: 'rgb(220,53,69)',
        iconColor: 'rgb(220,53,69)'
    }
};
let card = elements.create('card', {style: style});
card.mount('#card-element');
