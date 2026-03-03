Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from django.shortcuts import render
... from .models import Patient
... import datetime
... 
... def create_profile(request):
...     if request.method == "POST":
...         name = request.POST['name']
...         age = request.POST['age']
...         problem = request.POST['problem']
...         access = ",".join(request.POST.getlist('access'))
...         gender = request.POST['gender']
...         contact = request.POST['contact']
...         address = request.POST['address']
... 
...         blockchain = Blockchain()
... 
...         data = {
...             "name": name,
...             "age": age,
...             "problem": problem,
...             "access": access,
...             "gender": gender
...         }
... 
...         blockchain.add_new_transaction(data)
...         hash_value = blockchain.mine()
... 
...         Patient.objects.create(
...             patient_name=name,
...             age=age,
...             problem_desc=problem,
...             profile_date=datetime.datetime.now(),
...             access_data=access,
...             gender=gender,
...             contact_no=contact,
...             address=address,
...             blockchain_hash=hash_value,
            revenue=0
        )

        return render(request, "CreateProfile.html", {"msg": "Profile Created Successfully"})
    
