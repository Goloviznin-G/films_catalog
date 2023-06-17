from django import forms


def validate_date(value):
    if int(value) > 2023:
        raise forms.ValidationError(
            f'Вы определенно ошиблись с годом: {value}',
            params={'value': value},
        )


def validate_name(value):
    if value != 'aaa':
        raise forms.ValidationError(
            f'Вы определенно ошиблись с названием: {value}',
            params={'value': value},
        )
