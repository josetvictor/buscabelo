from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
from django.core import validators
from django.utils.translation import ugettext_lazy as _
import re


class UserManager(BaseUserManager):

	def create_superuser(self, email, username, password, **extra_fields):

		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must be assigned to is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must be assigned to is_superuser=True.')

		return self.create_user(email, username, password, **extra_fields)

	def create_user(self, email, username, password, **extra_fields):

		if not email:
		    raise ValueError(_('You must provide an email address'))

		
		email = self.normalize_email(email)
		user = self.model(email=email, username=username, **extra_fields)
		user.set_password(password)
		user.save()
		return user 		

class User(AbstractBaseUser, PermissionsMixin):

	class Types(models.TextChoices):
		CUSTOMER = "CUSTOMER", "Customer"
		PROVIDER = "PROVIDER", "Provider"

	base_type = Types.PROVIDER

	type = models.CharField(
	_("Type"), max_length=50, choices=Types.choices, default=base_type
	)

	avatar = models.ImageField(blank=True)

	username = models.CharField(_('username'), max_length=15, unique=False, help_text=_('Required. 15 characters or fewer. Letters, numbers and @/./+/-/_ characters'), validators=[ validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), _('invalid'))])    
	email = models.EmailField(_('email address'), max_length=255, unique=True)    
	
	is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Designates whether the user can log into this admin site.'))
	is_active = models.BooleanField(_('active'), default=True, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
	

	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

	objects = UserManager()
	
	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = ['username']

	def get_short_name(self):
		return self.username


	def save(self, *args, **kwargs):
	
		if not self.id:
			self.type = self.base_type
	
		return super().save(*args, **kwargs)


class CustomerManager(models.Manager):

	def get_queryset(self, *args, **kwargs):
		return super().get_queryset(*args, **kwargs).filter(type=User.Types.CUSTOMER)

class Customer(User):

	first_name= models.CharField(max_length=25, default='anon')
	last_name= models.CharField(max_length=25, default='anon')


	base_type = User.Types.CUSTOMER
	objects = CustomerManager()

	class Meta:
		verbose_name = _('customer')
		verbose_name_plural = _('customers')

class ProviderManager(models.Manager):
	def get_queryset(self, *args, **kwargs):
		return super().get_queryset(*args, **kwargs).filter(type=User.Types.PROVIDER)


class Provider(User):
	
	rating_average = models.FloatField()

	rating_number = models.IntegerField()

	base_type = User.Types.PROVIDER
	
	description = models.TextField()

	objects = ProviderManager()

	class Meta:
		verbose_name = _('provider')
		verbose_name_plural = _('providers')


class Comment(models.Model):
	description = models.TextField(max_length=255)
	provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

class Service(models.Model):
	provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
	name = models.CharField(_('service name'), max_length=30 )
	description = models.TextField( ('service description'), max_length=255)
	value = models.FloatField()

class ProviderGalleryImage(models.Model):
	provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
	image = models.ImageField()

class Appointment(models.Model):

	service = models.OneToOneField(Service, on_delete=models.CASCADE)

	client = models.ForeignKey(Customer, on_delete=models.CASCADE)

	shcheduled_date= models.DateTimeField(_('scheduled date'))

	appointment_date = models.DateTimeField(_('appointment date'))

	time_done_at = models.DateTimeField(_('time the work was finished'))

	canceled_at = models.DateTimeField(_('canceled at'), default = None, null = True)


