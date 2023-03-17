import React, { useState } from 'react';
import './Product.css';

const currencyOptions = {
  minimumFractionDigits: 2,
  maximumFractionDigits: 2,
}
const products = [
  {
    emoji: '🍦',
    name: 'ice cream',
    price: 5
  },
  {
    emoji: '🍩',
    name: 'donuts',
    price: 2.5,
  },
  {
    emoji: '🍉',
    name: 'watermelon',
    price: 4
  }
];

function getTotal(total) {
  return total.toLocaleString(undefined, currencyOptions)
}

export default function Product() {
  const [cart, setCart] = useState([]);
  const [total, setTotal] = useState(0);

  function add() {
    setCart(current => [...current, Product.name]);
    setTotal(current => current + Product.price);
  }
  function remove() {
    setCart (current => []);
    setTotal(current => current - Product.price);
  }
  return(
    <div className="wrapper">
      <div>
        Shopping Cart: {cart.length} total items.
      </div>
      <div>Total:{getTotal(total)}</div>
        <div>
        {products.map(product => (
          <div key={product.name}>
            <div className="product">
              <span role="img" aria-label={product.name}>{product.emoji}</span>
            </div>
            <button onClick={add}>Add</button>
            <button>Remove</button>
          </div>
        ))}
      </div>
    </div>
  )
}