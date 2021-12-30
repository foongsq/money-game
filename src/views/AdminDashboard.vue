<template>
  <div class="adminDashboard">
    <h1>Welcome Admin!</h1>
    <div class="addItemDiv">
      <h3>Add New Item To Store</h3>
       <!--Upload Image-->
      <form enctype="multipart/form-data">
        <div style="uploadImageTopDiv">
          <p class="uploadImageText">Upload item image</p>
          <p v-if="newItemImage">{{newItemImage}}</p>
        </div>
        <div v-if="!newItemImage" class="dropbox">
          <input type="file" @change="onImageChange($event.target.files)"
            accept="image/*" class="fileInput">
          <p v-if="isSaving">
            Uploading {{ fileCount }} files...
          </p>
          <p v-else>
            Drag your file(s) here to begin<br> or click to browse
          </p>
        </div>
      </form>
      <b-form-input class="adminInput" v-model="newItemName" placeholder="Enter item name"></b-form-input>
      <b-form-input class="adminInput" v-model="newItemPrice" type="number" placeholder="Enter item price"></b-form-input>
      <b-button class="adminButton" variant="light" @click="onReset">Reset</b-button>
      <b-button class="adminButton" variant="light" >Add Item</b-button>
    </div>
    <div class="storeDiv">
      <h3>Store</h3>
      <carousel-3d :autoplay="true" class="storeCarousel" :height="carouselHeight" :width="carouselWidth">
        <slide v-for="storeItem in store" :index="storeItem.itemId" :key="storeItem.itemId" class="storeSlides">
          <StoreItem 
            :itemName="storeItem.itemName" 
            :imgUrl="storeItem.imgUrl"
            :buyPrice="storeItem.buyPrice"
            :isAdmin="true" />
        </slide>
      </carousel-3d>
    </div>
    <div class="logoutButtonDiv">
      <button class="btn btn-secondary w-100">
        <router-link style="text-decoration: none; color: inherit;" to="/authentication">Logout</router-link>
      </button>
    </div>
  </div>
</template>

<script>
import StoreItem from '../components/StoreItem.vue';
import { Carousel3d, Slide } from 'vue-carousel-3d';

export default {
  name: 'AdminDashboard',
    components: {
    StoreItem, Carousel3d, Slide
  },
  computed: {
    carouselHeight: function () {
      return window.innerHeight * 0.23;
    },
    carouselWidth: function () {
      return Math.min(200, window.innerWidth * 0.3);
    }
  },
  data: function() {
    return {
      isInitial: true,
      isSaving: false,
      newItemImage: '',
      newItemName: '',
      newItemPrice: null,
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
    onImageChange(file) {
      // TODO: Send this file to backend to process and store
      console.log('file', file);
      this.isSaving = true;
      this.newItemImage = file[0].name;
      setTimeout(() => {this.isSaving = false;}, 1000) // To mimic saving
    },
    onReset() {
      this.newItemImage = '';
      this.newItemName = '';
      this.newItemPrice = null;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.adminDashboard {
  max-width: 600px;
  height: 100vh;
  padding: 1rem 0;
}

.addItemDiv {
  border: 1px solid grey;
  border-radius: 10px;
  padding: 1rem;
  margin: 0.5rem;
  background: var(--light-blue);
}

.adminInput {
  margin: 0.5rem 0;
}

.adminButton {
  margin: 0.5rem;
}

.uploadImageTopDiv {
  display: flex;
  justify-content: space-between;
}

.uploadImageText {
  text-align: left;
}

.dropbox {
  outline: 2px dashed grey; /* the dash box */
  outline-offset: -10px;
  background: rgb(224, 244, 255);
  color: dimgray;
  position: relative;
  cursor: pointer;
}

.fileInput {
  opacity: 0; /* invisible but it's there! */
  width: 100%;
  height: 100%;
  left: 0;
  position: absolute;
  cursor: pointer;
}

.dropbox:hover {
  background: lightblue; 
}

.dropbox p {
  text-align: center;
  padding: 1rem;
}
</style>
