import stripe

# Set your secret key. Remember to switch to your live secret key in production!
# See your keys here: https://dashboard.stripe.com/account/apikeys
stripe.api_key = 'pk_test_51I7K4uLcW4XlqZuyKRdxlZICS6mDQ5s9EiW6u8o33yEn8VkcIgNLMDnhMWupysTfCVgI7JyNmOv32GgVkz0jIarv00CAYfTpZu'


custom = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'name': 'T-shirt',
        },
        'unit_amount': 2000,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url= "https://yoursite.com/success.html",
    cancel_url='https://example.com/cancel',
  )

print(custom)



