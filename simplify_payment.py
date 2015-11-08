import simplify
simplify.public_key = "sbpb_MTVkN2ZhMmQtNTBiZi00MGYyLWIzOTEtODgxODBmYzU4MzU5"
simplify.private_key = "O8EOz5Z6doFeGDv/9cqSwJKaL6Ylu26x0VNxD7W1CJd5YFFQL0ODSXAOkNtXTToq"

#simplify access
def payment(token_id, amount):
    info  ={"amount":amount, "token_id":token_id, "currency":"USD","description":"app_test"}
    pay = simplify.Payment.create(info)

    if pay.paymentStatus == "APPROVED":
        return True
    return False
