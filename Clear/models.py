from django.db import models
from django.contrib.auth.models import User
import datetime

class UserProfile(models.Model):
    # CASCADE ensures that if a user is deleted, it deletes all things related to it

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(default=datetime.date.today)

    # PROTECT protects the deletion of a UserProfile if a Location is attemtped to be deleted, an error message is thrown

    #TODO move locations into a user locations table so the user can then have many locaitons
    current_loc = models.ForeignKey('Location', on_delete=models.PROTECT, related_name='current_users', null=True)
    home_loc = models.ForeignKey('Location', on_delete=models.PROTECT, related_name='home_users', null=True)
    work_loc = models.ForeignKey('Location', on_delete=models.PROTECT, related_name='work_users', null=True)
    other_loc = models.ForeignKey('Location', on_delete=models.PROTECT, related_name='other_users', null=True)
    pollution_limit = models.IntegerField()
    consent = models.BooleanField()


class Location(models.Model):
    postcode = models.CharField(max_length=12)
    name = models.CharField(max_length=128)


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


class UserInhaler(models.Model):
    # models.PROTECT works so if a user tries to delete an 'Inhaler' record (the one in quotations) then it wont let you
    # models.CASCADE will delete all related UserInhalers if a UserProfile (user) is deleted

    user_id = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='user_inhalers', null=False)
    inhaler_id = models.ForeignKey('Inhaler', on_delete=models.PROTECT, related_name='inhaler_users', null=False)
    puffs_today = models.IntegerField(default=0)
    puffs_remaining = models.IntegerField()

    # TODO Could this be done better?
    dose = models.IntegerField()
    puffs = models.IntegerField()
    frequency = models.IntegerField()

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
    band = models.CharField(max_length=128)
    lower_bound = models.IntegerField()
    upper_bound = models.IntegerField()
    general_description = models.CharField(max_length=512)
    risk_description = models.CharField(max_length=512)


class PollutionLevels(models.Model):
    loc_id = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='location_pollution', null=False)
    pollution_level = models.IntegerField()
    pollution_date = models.DateField(default=datetime.date.today)

    # The current flag will indicate the record that has the current pollution level for a specific region
    # (True = Current, False (0) = Previous). This allows us to build a history of pollution levels
    current_flag = models.BooleanField(default=True)

    def update_pollution_levels(self):
        # TODO Complete - when the table updates, will need to set all flags to false, and import all new, current,
        #  pollution levels to true
        pass
