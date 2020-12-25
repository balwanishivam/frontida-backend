from .models import MedicineInventory
import datetime
class CheckExpiry:
    def check(self,user):
        data=MedicineInventory.objects.filter(account=user)
        sys_date=datetime.date.today()
        expired_medicine=[]
        for medicine in data:
            if (medicine.expiry - sys_date) < datetime.timedelta(days=90):
                medicine.isexpired = True
                medicine.save()
                expired_medicine.append(medicine.name)
        return expired_medicine