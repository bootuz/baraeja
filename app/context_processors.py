from app.models import SocialMedia


def social_media(request):
    sm = SocialMedia.objects.all()
    return {"social_media": sm}
