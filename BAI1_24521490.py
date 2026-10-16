import numpy as np

# f = 4*x**4 - 6*x*y + y**2
def grad(u):
    x,y  = u
    return np.array([
        16*x**3 - 6*y,
        2*y - 6*x
    ])

def hessian(u):
    x, y = u
    return np.array([
        [48*x**2, -6],
        [-6, 2]
    ])

def newton_optim(u_0, grad_fn, hessian_fn, epsilon = 10e-8, max_iter = 100):
    u = u_0
    for _ in range(max_iter):
        grad = grad_fn(u)

        if np.linalg.norm(grad) < epsilon:
            return u

        hessian = hessian_fn(u)
    # t = grad @ np.linalg.inv(hessian)
        t = np.linalg.solve(hessian, -grad)

        u = u + t

    return u

if __name__ == '__main__':
    u_0 = (10, 10)
    u_optim = newton_optim(u_0, grad, hessian, max_iter = 100)
    print(u_optim)
