from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

from ckeditor.fields import RichTextField


def image_name(instance, filename):
    fname, extension = filename.split('.')
    try:
        slug = 'faculty/' + slugify(instance.full_name)
    except:
        pass
    try:
        slug = 'general/' + slugify(instance.filename)
    except:
        pass
    try:
        slug = 'time-tables-and-Attendance/' + slugify(instance.title)
    except:
        pass
    return '%s.%s' % (slug, extension)

class Faculty(models.Model):

    SHIFTS = (
         ('M', 'Morning'),
         ('E', 'Evening'),
    )

    CATEGORY = (
        ('office', 'Office Staff'),
        ('accounts', "Accounts"),
        ('library', "Library Staff"),
        ('placement', "Placement Staff"),
        ('teaching', "Teaching Faculty"),
    )

    full_name = models.CharField(max_length=200, verbose_name='Full Name', blank=False)
    profile_pic = models.ImageField(upload_to=image_name)
    category = models.CharField(max_length=30, choices=CATEGORY, default='teaching')
    designation = models.CharField(max_length=150, verbose_name='Designation', blank=False)
    phone_number = models.CharField(max_length=10, help_text='Phone Number (without Regional Code)', verbose_name='Phone Number', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    shift = models.CharField(max_length=1, choices=SHIFTS, default='M', verbose_name='Shift', help_text='Morning or Evening')
    department = models.CharField(max_length=100, verbose_name='Department', help_text='Eg. CSE / IT / EEE', blank=True, null=True)
    date_of_joining = models.DateField(null=True, blank=True, verbose_name='Date Of Joining')
    description = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'

    def __unicode__(self):
        return "%s" % self.full_name

class LatestNews(models.Model):
    title = models.CharField(max_length=250, help_text='Text to display')
    link = models.CharField(max_length=1000, help_text='Link for the News')
    new = models.BooleanField(default=True, help_text='This places a New Flag on th link')
    visible = models.BooleanField(default=True, help_text='Whether the News is Visible on Main Page')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Latest News'
        verbose_name_plural = 'Latest News'

    def __unicode__(self):
        return "%s" % self.title

class PrimaryMenu(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveSmallIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Primary Menu'
        verbose_name_plural = 'Primary Menus'

    def __unicode__(self):
        return "%s"  % self.name


class SecondaryMenu(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(PrimaryMenu, on_delete=models.CASCADE)
    link = models.CharField(max_length=1000)
    order = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Secondary Menu'
        verbose_name_plural = 'Secondary Menus'

    def __unicode__(self):
        return "%s > %s"  % (self.parent, self.name)

class TimeTable(models.Model):
    SHIFTS = (
         ('M', 'Morning'),
         ('E', 'Evening'),
    )
    title = models.CharField(max_length=50, help_text='Batch Name')
    shift = models.CharField(max_length=1, choices=SHIFTS)
    pdf = models.FileField(upload_to=image_name)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s"  % (self.title)

class Attendance(models.Model):
    SHIFTS = (
         ('M', 'Morning'),
         ('E', 'Evening'),
    )
    title = models.CharField(max_length=50, help_text='Batch Name')
    shift = models.CharField(max_length=1, choices=SHIFTS)
    pdf = models.FileField(upload_to=image_name)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s"  % (self.title)

class Syllabus(models.Model):
    title = models.CharField(max_length=50, help_text='Branch Name')
    pdf = models.FileField(upload_to=image_name)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s"  % (self.title)

class StudentSociety(models.Model):
    name = models.CharField(max_length=50, help_text='Society Name')
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s"  % (self.title)

class Achievement(models.Model):
    title = models.CharField(max_length=50, help_text='Tab Name')
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s"  % (self.title)

class Event(models.Model):
    title = models.CharField(max_length=50, help_text='Tab Name')
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s"  % (self.title)

class GeneralUpload(models.Model):
    filename = models.CharField(max_length=100, help_text='Eg: Campus Ground')
    files = models.FileField(upload_to=image_name)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s"  % (self.filename)
