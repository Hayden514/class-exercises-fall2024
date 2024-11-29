import React from 'react';
import { Form, Input, Button } from 'antd';

const FormComponent = ({ onSearch }) => {
  const onFinish = (values) => {
    onSearch(values);
  };

  return (
    <Form onFinish={onFinish} layout="inline" style={{ marginBottom: '20px' }}>
      <Form.Item
        name="searchTerm"
        rules={[{ required: true, message: 'Please enter a search term!' }]}
      >
        <Input placeholder="Search term" style={{ width: '200px' }} />
      </Form.Item>
      <Form.Item
        name="limit"
        rules={[{ required: true, message: 'Please enter a limit!' }]}
      >
        <Input
          placeholder="Limit (1-20)"
          type="number"
          min={1}
          max={20}
          style={{ width: '100px' }}
        />
      </Form.Item>
      <Form.Item>
        <Button type="primary" htmlType="submit">
          Search
        </Button>
      </Form.Item>
    </Form>
  );
};

export default FormComponent;
