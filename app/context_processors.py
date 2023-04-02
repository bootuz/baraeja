from app.models import SocialMedia


def social_media(request):
    sm = SocialMedia.objects.all()
    print(sm)
    return {"social_media": sm}
