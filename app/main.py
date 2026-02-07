import random
import matplotlib.pyplot as plt


def flip_coin():
    results = {}
    num_experiments = 10000

    for i in range(11):
        results[i] = 0

    for _ in range(num_experiments):
        heads_count = 0
        for _ in range(10):
            if random.random() < 0.5:
                heads_count += 1

        results[heads_count] += 1

    for key in results:
        results[key] = round(results[key] / num_experiments * 100, 2)

    return results


def draw_gaussian_distribution_graph():
    data = flip_coin()

    x_values = list(data.keys())
    y_values = list(data.values())

    plt.figure(figsize=(10, 7))
    plt.bar(x_values, y_values, color='purple', alpha=0.9, edgecolor='black')

    plt.xlabel('Количество орлов', fontsize=12)
    plt.ylabel('Процент случаев (%)', fontsize=12)
    plt.title('Распределение количества орлов при 10 подбрасываниях монеты\n(10000 экспериментов)', fontsize=14)
    plt.xticks(range(11))
    plt.grid(True, alpha=0.3)

    for i, v in enumerate(y_values):
        plt.text(i, v + 0.2, f'{v}%', ha='center', fontsize=9)

    plt.show()


print(flip_coin())
draw_gaussian_distribution_graph()