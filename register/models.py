from django.db import models

#회원가입 전 약관동의
class Agreement(models.Model): 
    #전체동의
    all_consent = models.CharField(max_length=200)
    #[필수]회원약관
    membership_terms = models.TextField(max_length=10000) 
    check_01 = models.CharField(max_length=200)
    #[필수]개인정보 수집 및 동의안내
    privacy = models.TextField(max_length=10000)
    check_02 = models.CharField(max_length=200)
    #[필수]개인정보 국외이전에 다한 동의
    overseas_transfer = models.TextField(max_length=10000)
    check_03 = models.CharField(max_length=200)
    #[선택]개인정보 제3자 제공에 대한 동의
    three_party = models.TextField(max_length=20000)
    check_04 = models.CharField(max_length=200)
    #[선택]마케팅 및 광고활용 동의
    marketing = models.TextField(max_length=10000)
    check_05 = models.CharField(max_length=200)





