<template>
  <div class="dashboard">
    <div class="userParticularsDiv">
      <div class="userNameDiv">
        <p>{{ username }}</p>
      </div>
      <div class="moneyDiv">
        <img className="moneyIcon" src="../assets/money-icon.jpg" height="20px"/>
        <p>{{ myMoney }}</p>
      </div>
    </div>
    <div class="myInventoryDiv">
      <h3>My Inventory</h3>
      <carousel-3d class="inventoryCarousel" :height="carouselHeight" :width="carouselWidth">
        <slide v-for="inventItem in myInventory" :index="inventItem.itemId" :key="inventItem.itemId" class="inventorySlides">
          <InventoryItem 
            :itemName="inventItem.itemName" 
            :imgUrl="inventItem.imgUrl"
            :sellPrice="inventItem.sellPrice"
            :quantity="inventItem.quantity" />
        </slide>
      </carousel-3d>
    </div>
    <div class="storeDiv">
      <h3>Store</h3>
      <carousel-3d :autoplay="true" class="storeCarousel" :height="carouselHeight" :width="carouselWidth">
        <slide v-for="(storeItem, index) in store" :index="index" :key="index" class="storeSlides">
          <StoreItem 
            :itemName="storeItem.itemName" 
            :img="storeItem.base64Img"
            :buyPrice="storeItem.buyPrice"
            :isAdmin="false" />
        </slide>
      </carousel-3d>
    </div>
    <div class="workButtonDiv">
      <button class="btn btn-success w-100" @click="onWork">Work (+10)</button>
    </div>
    <div class="logoutButtonDiv">
      <button class="btn btn-secondary w-100">
        <router-link style="text-decoration: none; color: inherit;" to="/authentication" >Logout</router-link>
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import StoreItem from '../components/StoreItem.vue';
import InventoryItem from '../components/InventoryItem.vue';
import { Carousel3d, Slide } from 'vue-carousel-3d';

export default {
  name: 'Dashboard',
  components: {
    StoreItem, InventoryItem, Carousel3d, Slide
  },
  computed: {
    carouselHeight: function () {
      return window.innerHeight * 0.23;
    },
    carouselWidth: function () {
      return Math.min(200, window.innerWidth * 0.3);
    }
  },
  data: function () {
    return {
      username: "user321",
      myMoney: 550,
      myInventory: [
        {
          itemId: 0,
          imgUrl: "../assets/chips.jpg",
          itemName: "chips1",
          sellPrice: 3,
          quantity: 1,
        },
        {
          itemId: 1,
          imgUrl: "../assets/chips.jpg",
          itemName: "chips2",
          sellPrice: 30,
          quantity: 1000,
        },
        {
          itemId: 2,
          imgUrl: "../assets/chips.jpg",
          itemName: "chips3",
          sellPrice: 300,
          quantity: 11,
        },
        {
          itemId: 3,
          imgUrl: "../assets/chips.jpg",
          itemName: "chipolata",
          sellPrice: 13,
          quantity: 10,
        },
      ],
      store: [
        {
          itemId: 0,
          imgUrl: "../assets/chips.jpg",
          itemName: "chips1",
          buyPrice: 3,
        },
        {
          itemId: 1,
          imgUrl: "../assets/chips.jpg",
          itemName: "chips2",
          buyPrice: 30,
        },
        {
          itemId: 2,
          imgUrl: "../assets/chips.jpg",
          itemName: "chips3",
          buyPrice: 300,
        },
        {
          itemId: 3,
          imgUrl: "../assets/chips.jpg",
          itemName: "chipolata",
          buyPrice: 13,
        },
      ],
    }
  },
  methods: {
    onWork() {
      this.myMoney += 10;
    }
  },
  created: async function() {
    await axios.get("/api/store").then((response) => {
      this.store = response.data;
      console.log("this.store", this.store);
    }, (error) => {
      console.log(error);
    });
  }
}
</script>

<!-- Not scoped because we want AdminDashboard to receive same styling for store -->
<style>
.dashboard {
  max-width: 600px;
  height: 100vh;
}

.userParticularsDiv {
  display: flex;
  justify-content: space-between;
  height: 5vh;
  margin-top: 0.5rem;
}

/* Need to flex in order to be able to center vertically using margin */
.userNameDiv {
  display: flex;
  margin: 0 1rem;
}

/* To center the money value vertically */
.userNameDiv p {
  margin: auto 0;
  padding: 0;
}

/* To put money icon and money value side by side */
.moneyDiv {
  display: flex;
  align-items: center;
  margin: 0 1rem;
}

.moneyIcon {
  max-height: 100%;
  max-width: 100%;
  display: block;
  height: auto;
  width: auto;
}

/* To center the money value vertically */
.moneyDiv p {
  margin: auto 0.5rem;
}

/*  - Add margin and padding around inventory
    - add black rounded border
    - yellow background color 
    - max height is 40vh*/
.myInventoryDiv {
  margin: 0.5rem;
  padding: 0.5rem;
  border: 1px solid black;
  border-radius: 10px;
  background: var(--light-yellow);
  max-height: 35vh;
}

/*  - Yellow background color,
    - rounded corners
    - box shadow */
.inventorySlides {
  background: var(--light-yellow);
  border-radius: 10px;
  box-shadow: 3px 3px 3px grey;
}

/* Change to lighter yellow when hover over carousel slide */
.inventorySlides:hover {
  background: var(--lighter-yellow);
}

/*  - Add margin and padding around inventory
    - add black rounded border
    - yellow background color */
.storeDiv {
  margin: 0.5rem;
  padding: 0.5rem;
  border: 1px solid black;
  border-radius: 10px;
  background: var(--light-purple);
  max-height: 35vh;
}

/* Add padding and margin to buttons */
.workButtonDiv, .logoutButtonDiv {
  padding: 0.5rem;
}

.logoutLink {
  text-decoration: none;
}

/* - Change background color of slide to purple
   - Round corners
   - Add box shadow */
.storeSlides {
  background: var(--light-purple);
  border-radius: 10px;
  box-shadow: 3px 3px 3px grey;
}

/* Change to lighter purple when hover over carousel slide */
.storeSlides:hover {
  background: var(--lighter-purple);
}
</style>
