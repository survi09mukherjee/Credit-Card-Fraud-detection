def credit_card_fraud_detector():
    card_number = input("Enter the credit card number: ")
    
    if len(card_number) != 16:
        print("Invalid credit card number length. Please enter a 16-digit number.")
        return
    
    sum_ = 0
    for i in range(0, 16):
        digit = int(card_number[i])
        if i % 2 == 0:
            digit *= 2
            digit = digit // 10 + digit % 10
        sum_ += digit
    
    if sum_ % 10 == 0:
        print("Valid credit card number.")
    else:
        print("Invalid credit card number.")
        
credit_card_fraud_detector()