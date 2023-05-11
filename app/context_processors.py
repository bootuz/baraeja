from app.forms import ContactForm
from app.models import SocialMedia


def social_media(request):
    sm = SocialMedia.objects.all()
    form = ContactForm()
    return {"social_media": sm, "form": form}
