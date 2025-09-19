from django.shortcuts import render,redirect
from .forms import SignUpForm,DepositForm,UserUpdateForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .models import User as UserModel
from transactions.models import Transaction as TransactionModel
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import os
import requests


load_dotenv()
# Create your views here.
# Store_ID=os.getenv('Store_ID')
# Store_Password=os.getenv('Store_Password')
# issandbox=os.getenv('issandbox')
# SSLZ_URL=os.getenv('SSLZ_URL')


class SignUpView(generic.FormView):
      template_name='signup_form.html'
      form_class=SignUpForm
      success_url=reverse_lazy("home")
      def dispatch(self, request, *args, **kwargs):
           if request.user.is_authenticated:
                return redirect('home')
           return super().dispatch(request, *args, **kwargs)
      def form_valid(self, form):
            user=form.save()
            return super().form_valid(form)
      
      
class LogInView(LoginView):
      template_name="login_form.html"
      def dispatch(self, request, *args, **kwargs):
           if request.user.is_authenticated:
                return redirect('home')
           return super().dispatch(request, *args, **kwargs)
      def get_success_url(self):
        return reverse_lazy('home')
      
      
class LogOutView(generic.View):
      def get(self,request):
           logout(request)
           return redirect('home')



class UserUpdateView(View):
    template_name = 'profile.html'

    def get(self, request):
        if request.user.is_authenticated:
            form = UserUpdateForm(instance=request.user)
            return render(request, self.template_name, {'form': form})
        else:
             return redirect('login')

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  
        return render(request, self.template_name, {'form': form})
    


def updateUserProfile(r):
    if r.user.is_authenticated:
       if r.method=='POST':
            data=r.POST
            # first_name=data['first_name']
            # last_name=data['last_name']
            contact_no=data['contact_no']
            user_image=r.FILES.get('user_image')
            user=UserModel.objects.get(user=r.user)
            #user
            user.user_image=user_image
            user.save()
            print(user_image)
            return redirect('update-user-profile')
       else:
          return render(r,'update_profile_t.html')
    else:
         return redirect('login')
    



def depositView(request):
     print(request.user.is_authenticated)
     if request.user.is_authenticated:
          if request.method=="POST":
               form=DepositForm(request.POST)
               if form.is_valid():
                  balance=form.cleaned_data['balance']
                  user=UserModel.objects.get(user=request.user)
                  user.balance+=balance
                  user.save()
                  TransactionModel.objects.create(user=request.user,amount=balance,transaction_type="Credit",payment_status="Pending",reference=None)

               #    payload = {
               #      "store_id": Store_ID,
               #      "store_passwd": Store_Password,
               #      "total_amount": balance,
               #      "currency": "BDT",
               #      "tran_id": f"TXN{request.user.id}{TransactionModel.objects.count()}",
               #      "success_url": request.build_absolute_uri("payment/success/"),
               #      "fail_url": request.build_absolute_uri("payment/fail/"),
               #      "cancel_url": request.build_absolute_uri("payment/cancel/"),
               #      "cus_name": request.user.username,
               #      "cus_email": request.user.email,
               #      "cus_add1": "Dhaka",
               #      "cus_city": "Dhaka",  
               #      "cus_country": "Bangladesh",
               #      "cus_phone": user.contact_no,
               #      "shipping_method": "NO",
               #      "product_name": "Wallet Deposit",
               #      "product_category": "Deposit",
               #      "product_profile": "general",
               #  }
               #    response = requests.post(SSLZ_URL, data=payload)
               #    data = response.json()
               #    print(data)
               #    if data.get("status") == "SUCCESS":
               #      TransactionModel.objects.create(user=request.user,amount=balance,transaction_type="Credit",payment_status="Pending",reference=payload["tran_id"])
               #      return redirect(data["GatewayPageURL"])
                  return redirect('home')
               else:
                    return render(request, "deposit_form.html", {"form": form, "error": "SSL Init Failed"})
          return render(request,'deposit_form.html',{'form':DepositForm()})
     else:
          return redirect('login')




# @csrf_exempt
# def payment_success(request):
#     amount = request.POST.get("amount")
#     tran_id = request.POST.get("tran_id") 
#     transaction=TransactionModel.objects.get(reference=tran_id)
#     user=UserModel.objects.get(user=transaction.user)
#     user.balance+=int(amount.split(".")[0])
#     user.save()
#     transaction.payment_status="Successful"
#     transaction.save()

#     return redirect('transaction_history')

# @csrf_exempt
# def payment_fail(request):
#     amount = request.POST.get("amount")
#     tran_id = request.POST.get("tran_id") 
#     transaction=TransactionModel.objects.get(reference=tran_id)
#     transaction.payment_status="Failed"
#     transaction.save()
#     return redirect('transaction_history')

# @csrf_exempt
# def payment_cancel(request):
#     amount = request.POST.get("amount")
#     tran_id = request.POST.get("tran_id") 
#     transaction=TransactionModel.objects.get(reference=tran_id)
#     transaction.payment_status="Cancelled"
#     transaction.save()
#     return redirect('transaction_history')

