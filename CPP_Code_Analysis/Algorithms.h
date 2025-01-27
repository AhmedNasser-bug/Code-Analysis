#pragma once
#include "Setup.h"

int func1(int n) {
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        cnt += 1;
    }
    return cnt;
}
int func2(int n) {
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cnt++;
        }
        cnt += func1(n);
    }
    return cnt;
}

int func3(int n) {
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        cnt += func2(n);
    }

    cnt+=func1(5000 * n);
    return cnt;
}

template<typename Func>
Func get_func(int func_name)
{
    Func funcs[] = { func1, func2, func3 };
    return *funcs[func_name];
}

