# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import math


class logistic_model:
    def __init__(self, n):
        self.theta = [1] * n

    def get(self, X):  # X 는 single list
        # linear multiply
        val = 0
        # except bias
        for k in range(len(X)):
            val += (X[k] * self.theta[k])
        return sigmoid(val)

    def reg(self):
        val = 0
        for i in range(len(self.theta) - 1):  # except bias term
            val += ((self.theta[i]) ** 2)
        return val


def solution(lr: float, threshold: float, l_val: float, beta1: float, beta2: float):
    get_input = sys.stdin.readline
    num_train = int(get_input().strip())  # 학습 데이터 개수

    train_data = []
    train_label = []

    # 학습 데이터 입력
    sum_x = []
    sum_y = []

    for i in range(num_train):
        x, y, t = list(map(float, get_input().strip().split()))
        train_data.append(to_feature_vector([x, y]))
        train_label.append(int(t))

    # do z-score normalization
    means, stds = normalize_each_dimension(train_data, num_train, len(train_data[-1]) - 1)

    # bias를 포함한 theta 생성
    model = logistic_model(len(train_data[-1]))

    batch_size = 256
    batch_step = num_train // batch_size
    if num_train % batch_size != 0:
        batch_step += 1

    # training part
    cost_diff = sys.maxsize
    prev = cost_function(train_data, train_label, model, l_val)

    v1 = [0] * (len(train_data[-1]))  # for momentum
    v2 = [0] * (len(train_data[-1]))  # for RMSProp
    time_step = 1
    while cost_diff > threshold:

        # get grad
        for i in range(batch_step):
            grad = [0] * (len(train_data[-1]))

            if num_train % batch_size != 0 and i == batch_step - 1:
                batched_train_data = train_data[i * batch_size:]
            else:
                batched_train_data = train_data[i * batch_size: (i + 1) * batch_size]

            for j in range(len(batched_train_data)):
                diff = (model.get(batched_train_data[j]) - train_label[j])
                for w in range(len(grad)):
                    grad[w] += (diff * batched_train_data[j][w])

            for w in range(len(grad)):
                grad[w] *= (1 / len(batched_train_data))
                if w != len(grad) - 1:  # bias term 만 제외하고 regulization term 추가
                    grad[w] += ((l_val / num_train) * model.theta[w])

            # update using adam
            for w in range(len(grad)):
                v1[w] = beta1 * v1[w] + (1 - beta1) * grad[w]
                v2[w] = beta2 * v2[w] + (1 - beta2) * (grad[w] ** 2)
                v1_b = v1[w] / (1 - (beta1 ** time_step))  # bias correlation
                v2_b = v2[w] / (1 - (beta2 ** time_step))
                model.theta[w] = model.theta[w] - lr * (v1_b / (math.sqrt(v2_b) + (10e-8)))

            time_step += 1.0
            curr = cost_function(train_data, train_label, model, l_val)
            cost_diff = abs(prev - curr)
            prev = curr
            print(curr)
            if cost_diff <= threshold:
                break

    num_test = int(get_input().strip())
    for j in range(num_test):
        x, y = list(map(float, get_input().strip().split()))
        test_single_data = to_feature_vector([x, y])
        normalize_test_data(test_single_data, means, stds)
        result = model.get(test_single_data)
        if result >= 0.5:
            print(1)
        else:
            print(0)


# 2차원의 경우
def to_feature_vector(input_data):
    x, y = input_data
    return [x, y, x ** 2, y ** 2, 1]


def normalize_each_dimension(train_data, num_of_train, features):
    # 각 차원마다 normalize 수행
    # output : 각 차원에 대한 mean, std, (마지막 bias term 제외)
    mean_data = [0] * (features)
    std_data = [0] * (features)

    # get mean data
    for i in range(num_of_train):
        for j in range(features):
            mean_data[j] += train_data[i][j]

    for i in range(features):
        mean_data[i] /= num_of_train

    # get std data
    for i in range(num_of_train):
        for j in range(features):
            std_data[j] += ((train_data[i][j] - mean_data[j]) ** 2)

    for i in range(features):
        std_data[i] = ((std_data[i] / num_of_train)) ** 0.5

    # do z-score normalize
    for i in range(num_of_train):
        for j in range(features):
            train_data[i][j] = (train_data[i][j] - mean_data[j]) / std_data[j]

    return mean_data, std_data


def normalize_test_data(test_data, means, stds):
    num_of_features = len(test_data) - 1
    for i in range(num_of_features):  # num_of_features
        test_data[i] = (test_data[i] - means[i]) / stds[i]


def cost_function(train_data, train_label, model, lg_val):
    cost = 0
    m = len(train_data)
    for k in range(len(train_data)):
        if train_label[k] == 1:
            cost += (-math.log(model.get(train_data[k])))
        else:  # 0
            cost += (-math.log(1 - model.get(train_data[k])))
    cost = (1 / m) * cost
    # add regularization term
    cost += ((lg_val / (2 * m)) * model.reg())

    return cost


def sigmoid(z):
    p = math.exp(-z)
    return (1 / (1 + p))


def get_std(f_list, mean):
    val = 0
    for f in f_list:
        val += ((f - mean) ** 2)
    return ((val / len(f_list)) ** 0.5)


beta1 = 0.9  # for momentum
beta2 = 0.999  # for RMSProp
learning_rate = 0.1
threshold = 10e-6
lambda_val = 1e-2
solution(learning_rate, threshold, lambda_val, beta1, beta2)