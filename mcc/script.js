
const foods = [
    {
        id: 1,
        name: "Cheese Pizza",
        category: "Pizza",
        price: 249,
        image: "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=500"
    },
    {
        id: 2,
        name: "Veg Burger",
        category: "Burger",
        price: 149,
        image: "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500"
    },
    {
        id: 3,
        name: "Cold Coffee",
        category: "Drinks",
        price: 99,
        image: "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=500"
    },
    {
        id: 4,
        name: "Farmhouse Pizza",
        category: "Pizza",
        price: 299,
        image: "https://images.unsplash.com/photo-1579751626657-72bc17010498?w=500"
    },
    {
        id: 5,
        name: "Chicken Burger",
        category: "Burger",
        price: 199,
        image: "https://images.unsplash.com/photo-1553979459-d2229ba7433a?w=500"
    },
    {
        id: 6,
        name: "Fresh Juice",
        category: "Drinks",
        price: 79,
        image: "https://images.unsplash.com/photo-1600271886742-f049cd451bba?w=500"
    }
];

let cart = [];

const foodContainer = document.getElementById("foodContainer");

// Display Food
function displayFoods(foodList) {
    foodContainer.innerHTML = "";

    foodList.forEach(food => {
        foodContainer.innerHTML += `
            <div class="col-md-4 col-sm-6">
                <div class="card food-card h-100">
                    <img src="${food.image}" class="card-img-top" alt="${food.name}">

                    <div class="card-body">
                        <h5>${food.name}</h5>
                        <p class="text-muted">${food.category}</p>

                        <div class="d-flex justify-content-between align-items-center">
                            <span class="price">₹${food.price}</span>

                            <button class="btn add-btn"
                                onclick="addToCart(${food.id})">
                                Add to Cart
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        `;
    });
}

// Filter Food
function filterFood(category) {
    const filtered = category === "All"
        ? foods
        : foods.filter(food => food.category === category);

    displayFoods(filtered);
}

// Search Food
document.getElementById("searchInput").addEventListener("input", function () {
    const value = this.value.toLowerCase();

    const filtered = foods.filter(food =>
        food.name.toLowerCase().includes(value)
    );

    displayFoods(filtered);
});

// Add to Cart
function addToCart(id) {
    const food = foods.find(item => item.id === id);
    const existing = cart.find(item => item.id === id);

    if (existing) {
        existing.quantity++;
    } else {
        cart.push({ ...food, quantity: 1 });
    }

    updateCart();
}

// Update Cart
function updateCart() {
    const cartItems = document.getElementById("cartItems");

    cartItems.innerHTML = "";

    let total = 0;
    let count = 0;

    cart.forEach(item => {
        total += item.price * item.quantity;
        count += item.quantity;

        cartItems.innerHTML += `
            <div class="d-flex justify-content-between align-items-center mb-3">
                <div>
                    <strong>${item.name}</strong>
                    <p class="mb-0">₹${item.price} × ${item.quantity}</p>
                </div>

                <div>
                    <button class="btn btn-sm btn-danger"
                        onclick="changeQuantity(${item.id}, -1)">-</button>

                    <button class="btn btn-sm btn-success"
                        onclick="changeQuantity(${item.id}, 1)">+</button>
                </div>
            </div>
        `;
    });

    if (cart.length === 0) {
        cartItems.innerHTML = "<p>Your cart is empty!</p>";
    }

    document.getElementById("cartCount").innerText = count;
    document.getElementById("cartTotal").innerText = total;
}

// Change Quantity
function changeQuantity(id, change) {
    const item = cart.find(item => item.id === id);

    if (!item) return;

    item.quantity += change;

    if (item.quantity <= 0) {
        cart = cart.filter(item => item.id !== id);
    }

    updateCart();
}

// Checkout
function checkout() {
    if (cart.length === 0) {
        alert("Your cart is empty!");
        return;
    }

    alert("Order placed successfully! (Demo)");

    cart = [];
    updateCart();

    bootstrap.Modal.getInstance(
        document.getElementById("cartModal")
    ).hide();
}

// Initial Display
displayFoods(foods);
updateCart();
