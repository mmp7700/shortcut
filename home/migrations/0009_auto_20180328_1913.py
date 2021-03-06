# Generated by Django 2.0.3 on 2018-03-28 19:13

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20180328_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField((('basicHeader', wagtail.core.blocks.StructBlock((('backgroundImage', wagtail.images.blocks.ImageChooserBlock()), ('headline', wagtail.core.blocks.TextBlock()), ('caption', wagtail.core.blocks.TextBlock()), ('buttonLeftText', wagtail.core.blocks.TextBlock()), ('buttonRightText', wagtail.core.blocks.TextBlock()), ('buttonLeftDestination', wagtail.core.blocks.PageChooserBlock(required=True)), ('buttonRightDestination', wagtail.core.blocks.PageChooserBlock(required=True))))), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('ItemCallout', wagtail.core.blocks.StreamBlock((('headline', wagtail.core.blocks.TextBlock()), ('caption', wagtail.core.blocks.TextBlock()), ('item', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.TextBlock()), ('caption', wagtail.core.blocks.TextBlock()))))))), ('MapInterstitial', wagtail.core.blocks.StructBlock(())), ('coloredInterstitial', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('topCaption', wagtail.core.blocks.TextBlock()), ('headline', wagtail.core.blocks.TextBlock()), ('button', wagtail.core.blocks.PageChooserBlock()), ('buttonText', wagtail.core.blocks.CharBlock())))), ('titleAndCaption', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.TextBlock()), ('caption', wagtail.core.blocks.TextBlock())))), ('GalleryInterstitial', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock()),)))), blank=True),
        ),
    ]
