def main():
    n, d = map(int, input().split())
    distances = []
    for _ in range(n):
        x, y = map(int, input().split())
        distance = (x**2 + y**2)**(1/2)
        distances.append(distance)
    print(len([distance for distance in distances if distance <= d]))


if __name__ == "__main__":
    main()
