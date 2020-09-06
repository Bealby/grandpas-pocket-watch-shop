/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

let stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
let client_secret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripe_public_key);
let elements = stripe.elements();
let style = {
    base: {
        color: 'rgb(0, 0, 0, 1)',
        fontFamily: '"Roboto", sans-serif',
        fontSize: '1.2rem',
        '::placeholder': {
            color: 'rgb(170, 186, 196)'
        }
    },
    invalid: {
        color: 'rgb(220,53,69,1)',
        iconColor: 'rgb(220,53,69,1)'
    }
};
let card = elements.create('card', {style: style});
card.mount('#card-element');