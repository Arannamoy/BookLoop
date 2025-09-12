from django.shortcuts import render,redirect
from .forms import SignUpForm,DepositForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import logout
from .models import User as UserModel
from transactions.models import Transaction as TransactionModel
# Create your views here.

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
     


def depositView(request):
     if request.user.is_authenticated:
          if request.method=="POST":
               form=DepositForm(request.POST)
               if form.is_valid():
                  balance=form.cleaned_data['balance']
                  user=UserModel.objects.get(user=request.user)
                  user.balance+=balance
                  user.save()
                  transaction=TransactionModel(user=request.user,amount=balance,transaction_type="Credit")
                  transaction.save()
                  return redirect('home')
          return render(request,'deposit_form.html',{'form':DepositForm()})
     else:
          return redirect('login')