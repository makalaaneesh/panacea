from __future__ import unicode_literals

from django.db import models


image_folder = "main/images/large"
thumbnail_folder = "main/images/thumbs"
profile_folder = "main/images/profile"



class Detail(models.Model):
	picture = models.ImageField(upload_to = profile_folder)
	about = models.TextField(max_length=10000, default="")
	
	
class Category(models.Model):
	name = models.CharField(max_length = 100)

	def __unicode__(self):              # __unicode__ on Python 2
		return self.name



# Create your models here.
class Painting(models.Model):
	# size, medium, price
	title = models.CharField(max_length=100, default="")
	description = models.TextField(max_length=10000, default="")
	image = models.ImageField(
		upload_to=image_folder
		)

	category = models.ManyToManyField(Category, related_name='paintings')

	thumbnail = models.ImageField(
		upload_to=thumbnail_folder,
		max_length=500,
		null=True,
		blank=True
		)

	def create_thumbnail(self):
		# original code for this method came from
		# http://snipt.net/danfreak/generate-thumbnails-in-django-with-pil/

		# If there is no image associated with this.
		# do not create thumbnail
		if not self.image:
			return


		from PIL import Image, ImageOps
		from cStringIO import StringIO
		from django.core.files.uploadedfile import SimpleUploadedFile
		import os

		# Set our max thumbnail size in a tuple (max width, max height)
		THUMBNAIL_SIZE = (250, 250)

		DJANGO_TYPE = self.image.file.content_type

		if DJANGO_TYPE == 'image/jpeg':
			PIL_TYPE = 'jpeg'
			FILE_EXTENSION = 'jpg'
		elif DJANGO_TYPE == 'image/png':
			PIL_TYPE = 'png'
			FILE_EXTENSION = 'png'

		# Open original photo which we want to thumbnail using PIL's Image
		image = Image.open(StringIO(self.image.read()))

		# We use our PIL Image object to create the thumbnail, which already
		# has a thumbnail() convenience method that contrains proportions.
		# Additionally, we use Image.ANTIALIAS to make the image look better.
		# Without antialiasing the image pattern artifacts may result.
		image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
		# image = ImageOps.fit(image, THUMBNAIL_SIZE, Image.ANTIALIAS)

		# Save the thumbnail
		temp_handle = StringIO()
		image.save(temp_handle, PIL_TYPE)
		temp_handle.seek(0)

		# Save image to a SimpleUploadedFile which can be saved into
		# ImageField
		suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
				temp_handle.read(), content_type=DJANGO_TYPE)
		# Save SimpleUploadedFile into image field
		self.thumbnail.save(
			'%s_thumbnail.%s' % (os.path.splitext(suf.name)[0], FILE_EXTENSION),
			suf,
			save=False
		)

	def save(self, *args, **kwargs):

		old_obj = Painting.objects.filter(id = self.id)
		if len(old_obj) == 0 or old_obj[0].image != self.image:
			print "Creating new thumbnail"
			self.create_thumbnail()

		force_update = False

		# If the instance already has been saved, it has an id and we set 
		# force_update to True
		if self.id:
			force_update = True

		# Force an UPDATE SQL query if we're editing the image to avoid integrity exception
		super(Painting, self).save(force_update=force_update)

	def __unicode__(self):              # __unicode__ on Python 2
		return self.image.url