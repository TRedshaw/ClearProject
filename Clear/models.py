from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

from django.http import request


class AppUser(AbstractUser):
    # CASCADE ensures that if a user is deleted, it deletes all things related to it
    # dob in form YYYY-MM-DD
    dob = models.DateField(default=datetime.date.today)
    # PROTECTs the deletion of a UserProfile if a Location is tried to be deleted
    current_location = models.ForeignKey('Location', on_delete=models.PROTECT, related_name='current_users', null=True)
    pollution_limit = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    consent = models.BooleanField()


    home_postcode = models.CharField(max_length=25)
    work_postcode = models.CharField(max_length=25,null=True,blank=True)
    other_postcode = models.CharField(max_length=25,null=True,blank=True)

    REQUIRED_FIELDS = ['dob', 'pollution_limit', 'consent']

    class Meta:
        verbose_name = 'App User'
        verbose_name_plural = 'App Users'
        ordering = ['id']

    def __str__(self):
        return self.username

    # TODO FIX
    def set_new_current_location(self):
        current_location = AppUser.objects.get(pk=id)
        current_location.current_location_id = 1  # change field
        current_location.save()  # this will update only

    def quick_set_current_location(self):
        # TODO For when they choose just work or other or home it gives them the pollution level by clicking
        #  button without having to enter their postcode

        # eg. if work clicked, then take the work location id from the userLocations table and insert into the current
        # location field in this table (for example)
        pass


    def add_location(self):
        # TODO Create code to add a location
        pass

    # TODO Add methods for editing username etc -- but wait to check if django has built in things for that
    #  so we dont need to add every function ourself


class UserLocations(models.Model):
    """
    Model which contains relationships between users and locations for location types other than current. Table produced
    so that the user can have many other common locations.
    """

    # The first element in each tuple is the value that will be stored in the database.
    # The second element is displayed by the field’s form widget.

    LOCATION_TYPES = [
        ('home', 'Home'),
        ('work', 'Work'),
        ('other', 'Other')
    ]

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='locations_user', null=False)
    location_id = models.ForeignKey('Location', on_delete=models.PROTECT, related_name='users_location', null=True)
    location_type = models.CharField(max_length=5, choices=LOCATION_TYPES)

    class Meta:
        verbose_name = 'User Location'
        verbose_name_plural = 'User Locations'
        ordering = ['id']

    def __str__(self):
        return_string = str(self.user_id) + "@" + str(self.location_type)
        return return_string


class Location(models.Model):
    """
    A model which contains all location names and their related postcodes. Will be used to associate
    location name with ID.
    """
    postcode = models.CharField(max_length=12)
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
        ordering = ['postcode']

    def __str__(self):
        return self.name


class Inhaler(models.Model):
    name = models.CharField(max_length=12)

    # TODO consider normalising this table into 3 separate (dosage, strength, inhaler) to relate better
    low_dose = models.IntegerField()  # 100 micrograms
    low_puffs = models.IntegerField()  # 2 puffs
    low_frequency = models.IntegerField()  # twice a day

    med_dose = models.IntegerField()
    med_puffs = models.IntegerField()
    med_frequency = models.IntegerField()

    hi_dose = models.IntegerField()
    hi_puffs = models.IntegerField()
    hi_frequency = models.IntegerField()

    class Meta:
        verbose_name = 'Inhaler'
        verbose_name_plural = 'Inhalers'
        ordering = ['id']

    def __str__(self):
        return self.name


class UserInhaler(models.Model):
    # Adding inhaler type to the inhaler page so user can know which inhaler they are tracking
    inhaler_type = [
        ('Beclametasone_dipropionate', 'Beclametasone dipropionate'),
        ('Ciclesonide', 'Ciclesonide'),
        ('Fluticasone_poprionate', 'Fluticasone poprionate'),
        ('Beclometasone', 'Beclometasone'),
        ('Budesonide', 'Budesonide'),
        ('Fluticasone_poprionate', 'Fluticasone_poprionate'),
        ('Mometasone', 'Mometasone'),
        ('Beclometasone_dipropionate_with_ormoterol', 'Beclometasone_dipropionate_with_ormoterol'),
        ('Budesonid_with_formoterol', 'Budesonid_with_formoterol'),
        ('Fluticasone_poprionate_with_formoterol', 'Fluticasone_poprionate_with_formoterol'),
        ('Fluticasone_poprionate_with_salmeterol', 'Fluticasone_poprionate_with_salmeterol'),
        ('Fluticasone_furoate_with_vilanterol', 'Fluticasone_furoate_with_vilanterol'),
    ]
    # models.PROTECT works so if a user tries to delete an 'Inhaler' record (the one in quotations) then it wont let you
    # models.CASCADE will delete all related UserInhalers if a UserProfile (user) is deleted

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='inhalers_user', null=False)
    # inhaler_id = models.ForeignKey('Inhaler', on_delete=models.PROTECT, related_name='users_inhaler', null=False)
    inhaler_type = models.CharField(max_length=200, choices=inhaler_type)
    puffs_today = models.IntegerField(default=0)
    puffs_remaining = models.IntegerField(null=False)
    puffs_per_day = models.IntegerField(null=True, blank=True)

    dose = models.IntegerField(help_text='Dose in micrograms', null=True, blank=True)
    puffs = models.IntegerField(help_text='Number of puffs per usage', null=True, blank=True)
    frequency = models.IntegerField(help_text='Number of uses per day',default=0)
    updated_at = models.DateTimeField(auto_now=True)  # attributes time
    class Meta:
        verbose_name = 'User Inhaler'
        verbose_name_plural = 'Users Inhalers'
        ordering = ['id']

    def __str__(self):
        return_string = str(self.user_id) + " with " + str(self.inhaler_type)
        return return_string
    def get_readable_type(self):
        return self.inhaler_type.replace('_', ' ')

    def add_inhaler(self):
        # TODO Complete
        pass

    # To reset puffs today to zero every day:
    def get_puffs_today(self):
        today_date = datetime.date.today()
        # today_date = '2023-01-10'
        if self.updated_at.strftime('%Y-%m-%d') != str(today_date):
            self.puffs_today = 0
            self.save()


    def delete_inhaler(self):
        # TODO Complete
        pass


    def log_puff(user_inhaler_id):
        user_inhaler = UserInhaler.objects.get(pk=user_inhaler_id)
        if user_inhaler.puffs_remaining > 0:
            user_inhaler.puffs_today += 1  # change field
            user_inhaler.puffs_remaining -= 1

            user_inhaler.save()  # this will update only
            return 1
        return None
class Inhalers(models.Model):
    inhaler_type = [
        ('Beclametasone_dipropionate', 'Beclametasone_dipropionate'),
        ('Ciclesonide', 'Ciclesonide'),
        ('Fluticasone_poprionate', 'Fluticasone_poprionate'),
        ('Beclometasone', 'Beclometasone'),
        ('Budesonide', 'Budesonide'),
        ('Fluticasone_poprionate', 'Fluticasone_poprionate'),
        ('Mometasone', 'Mometasone'),
        ('Beclometasone_dipropionate_with_ormoterol', 'Beclometasone_dipropionate_with_ormoterol'),
        ('Budesonid_with_formoterol', 'Budesonid_with_formoterol'),
        ('Fluticasone_poprionate_with_formoterol', 'Fluticasone_poprionate_with_formoterol'),
        ('Fluticasone_poprionate_with_salmeterol', 'Fluticasone_poprionate_with_salmeterol'),
        ('Fluticasone_furoate_with_vilanterol', 'Fluticasone_furoate_with_vilanterol'),
    ]

    remaing_puff_choice = (
        ('10', '10'),
        ('20', '20'),
        ('30', '30'),
        ('40', '40'),
        ('50', '50'),
        ('60', '60'),
        ('70', '70'),
        ('80', '80'),
        ('90', '90'),
        ('100','100'),
    )
    puffs_per_Day = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10','10'),
    )


    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='inhaler_user', null=False)
    inhaler_type = models.CharField(max_length=200, choices=inhaler_type)
    puffs_remaining = models.CharField(max_length=20, choices=remaing_puff_choice)
    puffs = models.CharField(max_length=200, choices=puffs_per_Day)
    per_Day = models.CharField(max_length=20, choices=puffs_per_Day)

class PollutionLevelInfo(models.Model):
    band = models.CharField(max_length=6)
    lower_bound = models.IntegerField()
    upper_bound = models.IntegerField()
    general_description = models.CharField(max_length=512)
    risk_description = models.CharField(max_length=512)

    class Meta:
        verbose_name = 'Pollution Level Info'
        verbose_name_plural = 'Pollution Level Info'
        ordering = ['id']

    def __str__(self):
        return self.band


class PollutionLevels(models.Model):
    # TODO will need to edit at a later date to accomodate for different pollutants
    location_id = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='location_pollution', null=False)
    pollution_level = models.IntegerField()
    pollution_date = models.DateField(default=datetime.date.today)

    # The current flag will indicate the record that has the current pollution level for a specific region
    # (True = Current, False (0) = Previous). This allows us to build a history of pollution levels
    current_flag = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Pollution Levels'
        verbose_name_plural = 'Pollution Levels'
        ordering = ['location_id']

    def __str__(self):
        return_string = "Level " + str(self.pollution_level) + "@" + str(self.location_id)
        return return_string

    def update_pollution_levels(self):
        # TODO Complete - when the table updates, will need to set all flags to false, and import all new, current,
        #  pollution levels to true
        pass

class Boroughs(models.Model):
    OutwardName = models.CharField(max_length=128)
    ApiName = models.CharField(max_length=128)

class Meta:
    verbose_name = 'Boroughs'
    verbose_name_plural = 'Boroughs'
    ordering = ['ApiName']

def __str__(self):
    return self.OutwardName


