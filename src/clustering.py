
import csv, random, math

def load_runs(path):
    X = []
    with open(path, newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)
        for row in r:
            X.append([float(row['team1_runs']), float(row['team2_runs'])])
    return X

def d(a,b): return math.hypot(a[0]-b[0], a[1]-b[1])

def kmeans(X, k=3, iters=10, seed=0):
    random.seed(seed)
    centers = random.sample(X, k)
    for _ in range(iters):
        clusters = [[] for _ in range(k)]
        for x in X:
            idx = min(range(k), key=lambda i: d(x, centers[i]))
            clusters[idx].append(x)
        new_centers = []
        for i in range(k):
            if clusters[i]:
                cx = sum(p[0] for p in clusters[i]) / len(clusters[i])
                cy = sum(p[1] for p in clusters[i]) / len(clusters[i])
                new_centers.append([cx, cy])
            else:
                new_centers.append(centers[i])
        if all(d(centers[i], new_centers[i]) < 1e-6 for i in range(k)): break
        centers = new_centers
    labels = [min(range(k), key=lambda i: d(x, centers[i])) for x in X]
    return centers, labels

if __name__ == "__main__":
    X = load_runs("data/ipl_matches.csv")
    centers, labels = kmeans(X, 3)
    print("centers:", centers)
    print("labels[:10]:", labels[:10])
