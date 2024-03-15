#!/usr/bin/env/ python3 
# -*- coding:UTF-8 -*-
# @Time      :2024/3/15 16:34
# @Author    :Si Nian
# @Software  :PyCharm
import pytest
import requests

# 定义基础URL
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    """测试获取帖子列表"""
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_post():
    """测试获取单个帖子"""
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    assert response.json()['id'] == 1

def test_create_post():
    """测试创建帖子"""
    data = {
        "title": 'foo',
        "body": 'bar',
        "userId": 1,
    }
    response = requests.post(f"{BASE_URL}/posts", data=data)
    assert response.status_code == 201
    assert response.json()['title'] == 'foo'

def test_update_post():
    """测试更新帖子"""
    data = {
        "id": 1,
        "title": 'updated title',
        "body": 'updated body',
        "userId": 1,
    }
    response = requests.put(f"{BASE_URL}/posts/1", data=data)
    assert response.status_code == 200
    assert response.json()['title'] == 'updated title'

def test_delete_post():
    """测试删除帖子"""
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

if __name__ == "__main__":
    pytest.main()
