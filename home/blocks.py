from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock, PageChooserBlock
)

class FullPageIntro(StructBlock):
    backgroundImage = ImageChooserBlock()
    headline = TextBlock()
    caption = TextBlock()
    buttonLeftText = TextBlock()
    buttonRightText = TextBlock()
    buttonLeftDestination = PageChooserBlock(required=True)
    buttonRightDestination = PageChooserBlock(required=True)

    class Meta:
        template = 'blocks/full-page.html'

class ParagraphText(StructBlock):
    text = RichTextBlock()

    class Meta:
        template = 'blocks/paragraph-text.html'


class TitleAndCaption(StructBlock):
    headline = TextBlock()
    caption = TextBlock()

    class Meta:
        template = 'blocks/title-and-caption.html'


class GalleryInterstitial(StreamBlock):
    image = ImageChooserBlock()

    class Meta:
        template = 'blocks/interstitial-gallery.html'


class coloredInterstitial(StructBlock):
    image = ImageChooserBlock()
    topCaption = TextBlock()
    headline = TextBlock()
    button = PageChooserBlock()
    buttonText = CharBlock()

    class Meta:
        template = 'blocks/colored-interstitial.html'


class BasicHeaderBackground(StructBlock):
    backgroundImage = ImageChooserBlock(required=True)
    headline = TextBlock(required=False)
    caption = TextBlock(required=False)
    buttonLeftText = TextBlock(required=False)
    buttonRightText = TextBlock(required=False)
    buttonLeftDestination = PageChooserBlock(required=False)
    buttonRightDestination = PageChooserBlock(required=False)

    class Meta:
        template = 'blocks/basic-header.html'


class MapInterstitial(StructBlock):

    class Meta:
        template = 'blocks/map-interstitial.html'


class ItemForOptions(StructBlock):
    image = ImageChooserBlock()
    title = TextBlock()
    caption = TextBlock()

    class Meta:
        template = 'blocks/item-block.html'


class HeadlineCaptionOptions(StreamBlock):
    headline = TextBlock()
    caption = TextBlock()
    item = ItemForOptions()

    class Meta:
        template = 'blocks/HeadlineCaptionOptions.html'


# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """
    fullHeader = FullPageIntro()
    basicHeader = BasicHeaderBackground()
    embed = EmbedBlock()
    paragraph = ParagraphText()
    ItemCallout = HeadlineCaptionOptions()
    MapInterstitial = MapInterstitial()
    coloredInterstitial = coloredInterstitial()
    titleAndCaption = TitleAndCaption()
    GalleryInterstitial = GalleryInterstitial()
