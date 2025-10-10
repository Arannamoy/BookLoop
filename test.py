class Book(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField(null=True)
    author=models.CharField(max_length=150,null=True)
    add_date=models.DateTimeField(auto_now_add=True,null=True)
    borrow_price=models.DecimalField(decimal_places=2,max_digits=12,null=True)
    book_image=models.ImageField(upload_to="book_image",null=True)
    added_by=models.ForeignKey(UserModel,related_name="user_add",on_delete=models.CASCADE)
    category=models.ManyToManyField(CategoryModel,related_name="book_categories")
    quantity=models.IntegerField(null=True)
    total_borrowed_time=models.IntegerField(default=0,null=True)


class Borrow_record(models.Model):
    user = models.ForeignKey (UserModel,related_name="user_borrow_record",on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel,on_delete=models.CASCADE)
    borrow_date=models.DateTimeField(null=True)
    return_status=models.CharField(choices=RETURN_STATUS,null=True)
    due_date=models.DateTimeField(null=True)
    return_date =models.DateTimeField(null=True,blank=True)
    created_at =models.DateTimeField(auto_now=True,null=True)
    review_status=models.BooleanField(default=False)

class Category(models.Model):
      title=models.CharField(max_length=150,null=True)
      added_by=models.ForeignKey(UserModel,on_delete=models.CASCADE)
      add_date=models.DateTimeField(auto_now=True)
      slug=models.SlugField(max_length=100,null=True,unique=True,blank=True)


class Discussion(models.Model):
    user=models.ForeignKey(User,related_name="user_discussions",on_delete=models.CASCADE)
    book=models.ForeignKey(Book,related_name="book_discussions",on_delete=models.CASCADE)
    comment=models.TextField(null=True)
    discussion_image=models.ImageField(upload_to="discussion_image",null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    user=models.ForeignKey(User,related_name="user_reviews",on_delete=models.CASCADE)
    book=models.ForeignKey(Book,related_name="book_reviews",on_delete=models.CASCADE)
    borrow_record=models.OneToOneField(Borrow_record,null=True,related_name="borrow_reviews",on_delete=models.CASCADE)
    rating=models.CharField(choices=RATING,null=True)
    comment=models.TextField(null=True,blank=True)
    review_image=models.ImageField(upload_to="review_image",null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
      user=models.ForeignKey(UserModel,related_name="user_transaction",on_delete=models.CASCADE)
      amount=models.FloatField(null=True)
      transaction_type=models.CharField(choices=TRANSACTION_TYPE,null=True)
      payment_status=models.CharField(choices=PAYMENT_STATUS,null=True)
      created_at=models.DateTimeField(auto_now=True,null=True)
      reference=models.CharField(max_length=500,null=True)

class User(models.Model):
    user=models.OneToOneField(User,related_name="user_acc",on_delete=models.CASCADE)
    email=models.EmailField(unique=True,null=True)
    contact_no=models.CharField(max_length=11,unique=True,null=True)
    borrowed_books=models.ManyToManyField(Book, related_name='borrowed_books', blank=True)
    gender=models.CharField(max_length=20,choices=GENDER,null=True)
    deposit_date=models.DateField(auto_now_add=True,null=True)
    balance=models.DecimalField(decimal_places=2,max_digits=12,default=0,null=True)
    dob=models.DateField(null=True)
    joining_time=models.DateTimeField(auto_now=True,null=True)
    user_image=models.ImageField(upload_to="user_image",null=True,blank=True)
    user_type=models.CharField(choices=USER_TYPE,null=True,default="USER")


