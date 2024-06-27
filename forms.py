from django import forms


# Form нужна что бы отправить какие то данные в БД
class SearchForm(forms.Form):
    search = forms.CharField(max_length=256)

# На след уроке тут должны создать авторизацию(Регистрация/Логин)
