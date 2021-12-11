from allauth.account.adapter import DefaultAccountAdapter
from .models import Contracts


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)

        contract_data = request.data.get('contract')
        if contract_data:
            contract = Contracts.objects.get(pk=contract_data)
            user.contract = contract
        user.first_name = request.data.get('first_name')
        user.last_name = request.data.get('last_name')
        user.three_name = request.data.get('three_name')
        user.address = request.data.get('address')
        user.customers_type = request.data.get('customers_type')
        user.avatar = request.data.get('avatar')
        user.about = request.data.get('about')
        user.company = request.data.get('company')
        user.inn = request.data.get('inn')
        user.ogrn = request.data.get('ogrn')

        user.save()
        return user