import { render, screen, fireEvent } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import App from './App';

describe('App', () => {
  it('renders header correctly', () => {
    render(<App />);
    expect(screen.getByText('Data-Continuum Logistics')).toBeDefined();
  });

  it('allows user to type shipment ID', () => {
    render(<App />);
    const input = screen.getByPlaceholderText('Enter Shipment ID');
    fireEvent.change(input, { target: { value: '123' } });
    expect(input.value).toBe('123');
  });
});
