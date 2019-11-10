from django import forms

class AgreementForm(forms.ModelForm):
    #전체동의
    CHOICES=[('전체동의','전체동의')]
    all_consent = forms.ChoiceField(label='전체동의', widget=forms.RadioSelect, choices=CHOICES)
    
    #[필수]회원약관
    CHOICES=[('회원약관에 동의합니다','회원약관에 동의합니다')]
    membership_terms = forms.CharField(label='[필수]회원약관') 
    check_01 = forms.ChoiceField(label='회원약관에 동의합니다', widget=forms.RadioSelect, choices=CHOICES)
    
    #[필수]개인정보 수집 및 동의안내
    CHOICES=[('개인정보 수집 및 이용에 동의합니다','개인정보 수집 및 이용에 동의합니다')]
    privacy = forms.CharField(label='[필수]개인정보 수집 및 동의안내')
    check_02 = forms.ChoiceField(label='개인정보 수집 및 이용에 동의합니다', widget=forms.RadioSelect, choices=CHOICES)
    
    #[필수]개인정보 국외이전에 대한 동의
    CHOICES=[('개인정보 국외이전에 동의합니다','개인정보 국외이전에 동의합니다')]
    overseas_transfer = forms.CharField(label='[필수]개인정보 국외이전에 대한 동의')
    check_03 = forms.ChoiceField(label='개인정보 국외이전에 동의합니다', widget=forms.RadioSelect, choices=CHOICES)
    
    #[선택]개인정보 제3자 제공에 대한 동의
    CHOICES=[('개인정보 제3자 제공에 동의합니다(선택사항)','개인정보 제3자 제공에 동의합니다(선택사항)')]
    three_party = forms.CharField(label='[선택]개인정보 제3자 제공에 대한 동의')
    check_04 = forms.ChoiceField(label='개인정보 제3자 제공에 동의합니다(선택사항)', widget=forms.RadioSelect, choices=CHOICES)
    
    #[선택]마케팅 및 광고활용 동의
    CHOICES=[('마케팅 광고 및 활용에 동의합니다','마케팅 광고 및 활용에 동의합니다')]
    marketing = forms.CharField(label='[선택]마케팅 및 광고활용 동의')
    check_05 = forms.ChoiceField(label='마케팅 광고 및 활용에 동의합니다', widget=forms.RadioSelect, choices=CHOICES)
