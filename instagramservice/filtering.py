from instagramservice.models import InstagramPostFact, Fact


def get_facts_queryset():

    published_posts = InstagramPostFact.objects.filter(is_published=True).order_by('-published_date')

    if len(published_posts) >= 3:
        amount = 3
    elif len(published_posts) == 2:
        amount = 2
    elif len(published_posts) == 1:
        amount = 1
    else:
        amount = 0

    facts_not_used = [obj.id for obj in Fact.objects.all() if obj.is_used == False]
    facts = Fact.objects.filter(id__in=facts_not_used)

    facts_priority = facts.exclude(priority=None)


    print('FAKTY:', facts)
    print('AMOUNT:', amount)
    excluded_places = []
    for x in range(amount):
        last_post_place = published_posts[x].fact.place
        print('LAST PLACE:', last_post_place)
        if facts.exclude(place__in=excluded_places).exclude(place=last_post_place):
            excluded_places.append(last_post_place)
            print('DODANE DO EXCLUDED:', last_post_place)
        else:
            break

    facts_filtered = facts.filter(priority=None).exclude(place__in=excluded_places)
    facts_rest = facts.exclude(pk__in=facts_priority).exclude(pk__in=facts_filtered)
    combined_queryset = facts_priority | facts_filtered | facts_rest
    return combined_queryset

