from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class AppUser(AbstractUser):
    # CASCADE ensures that if a user is deleted, it deletes all things related to it
    dob = models.DateField(default=datetime.date.today)
    # PROTECTs the deletion of a UserProfile if a Location is tried to be deleted
    current_location = models.ForeignKey('Location', on_delete=models.PROTECT, related_name='current_users', null=True)
    pollution_limit = models.IntegerField()
    consent = models.BooleanField()

    REQUIRED_FIELDS = ['dob', 'pollution_limit', 'consent']

    class Meta:
        verbose_name = 'App User'
        verbose_name_plural = 'App Users'
        ordering = ['id']

    def __str__(self):
        return self.username

    def set_new_current_location(self):
        # TODO set it so when the user enters their current location, it updates the current location field
        pass

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

    user_id = models.ForeignKey('AppUser', on_delete=models.CASCADE, related_name='locations_user', null=False)
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
    # models.PROTECT works so if a user tries to delete an 'Inhaler' record (the one in quotations) then it wont let you
    # models.CASCADE will delete all related UserInhalers if a UserProfile (user) is deleted

    user_id = models.ForeignKey('AppUser', on_delete=models.CASCADE, related_name='inhalers_user', null=False)
    inhaler_id = models.ForeignKey('Inhaler', on_delete=models.PROTECT, related_name='users_inhaler', null=False)
    puffs_today = models.IntegerField(default=0)
    puffs_remaining = models.IntegerField(null=False)

    dose = models.IntegerField(help_text='Dose in micrograms')
    puffs = models.IntegerField(help_text='Number of puffs per usage')
    frequency = models.IntegerField(help_text='Number of uses per day')

    class Meta:
        verbose_name = 'User Inhaler'
        verbose_name_plural = 'Users Inhalers'
        ordering = ['id']

    def __str__(self):
        return_string = str(self.user_id) + " with " + str(self.inhaler_id)
        return return_string

    def add_inhaler(self):
        # TODO Complete
        pass

    def edit_inhaler(self):
        # TODO Complete
        pass

    def delete_inhaler(self):
        # TODO Complete
        pass


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
