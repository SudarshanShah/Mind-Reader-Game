from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")


def game(request):
    if request.method == "POST":
        name = request.POST['name']
        context = {'cards': card_game(), 'name': name}
        return render(request, "game.html", context)
    else:
        return render(request, "home.html")


def get_binary_digits(num):
    bin_list = []
    while num > 0:
        bin_list.append(num % 2)
        num = num // 2
    # bin_list.reverse()
    return bin_list


def card_game():
    cards = [[], [], [], [], [], []]
    for i in range(1, 64):
        bin_list = get_binary_digits(i)
        for j in range(len(bin_list)):
            if (bin_list[j] * (2 ** j)) != 0:
                cards[j].append(i)

    return cards
