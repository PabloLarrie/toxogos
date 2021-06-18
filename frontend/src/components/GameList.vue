<template>
  <table-layout>
    <template v-slot:pagination-top>
      <table-pagination
        :next="next"
        :previous="previous"
        v-model="filters.size"
        @nextPageClick="nextPage"
        @previousPageClick="previousPage"
      />
    </template>
    <template v-slot:filters>
      <b-button-toolbar>

        <b-input
          size="sm"
          class="mr-sm-2"
          placeholder="Search by game name"
          v-model="searchInfo"
          debounce="500"
        ></b-input>

        <b-form-select
            v-model="filters.selectedType"
            :options="typeOptions"
        >
        </b-form-select>

        <b-form-select
          v-model="filters.selectedMinPlayers"
          :options="minPlayersOptions"
        >
        </b-form-select>

        <b-form-select
          v-model="filters.selectedMaxPlayers"
          :options="maxPlayersOptions"
        >
        </b-form-select>

        <b-form-select
            v-model="filters.selectedDuration"
            :options="durationOptions"
        >
        </b-form-select>

        <b-form-select
            v-model="filters.selectedAge"
            :options="AgeOptions"
        >
        </b-form-select>

        <b-form-select
          class="mr-sm-5 w-25 h-25"
          v-model="filters.selectedDesigner"
          :options="designerOptions"
        >
        </b-form-select>

        <b-button @click="resetFilter"> Reset </b-button>
      </b-button-toolbar>

    </template>

    <template v-slot:table>
      <b-table
        class="w-100"
        striped
        hover
        fixed
        noCollapse
        :items="info"
        :fields="columns"
        bordered
        @row-clicked="rowClick"
      >
        <template #cell(heroes)="data">
          {{ data.value.length ? data.value.join(", ") : "Neutral" }}
        </template>
        <template #cell(expansion)="data">
          {{ data.value.join(", ") }}
        </template>
      </b-table>
    </template>

    <template v-slot:pagination-bottom>
      <table-pagination
        :next="next"
        :previous="previous"
        v-model="filters.size"
        @nextPageClick="nextPage"
        @previousPageClick="previousPage"
      />
    </template>
  </table-layout>
</template>

<script>
import TablePagination from "@/components/table/TablePagination";
import TableLayout from "@/layouts/TableLayout";

export default {
  name: "CardsList",
  components: {
    TablePagination,
    TableLayout,
  },
  data() {
    return {
      info: [],
      next: null,
      previous: null,
      savedFilters: {},
      searchInfo: null,
      columns: [
        "name",
        "game_type",
        "description",
        "min_players",
        "max_players",
        "duration",
        "min_age",
        "designer",
      ],
      filters: {
        selectedExpansion: "",
        selectedMinPlayers: "",
        selectedMaxPlayers: "",
        selectedDuration: "",
        selectedAge: "",
        selectedType: "",
        selectedDesigner: "",
        size: 15,
      },
      typeOptions: [
        { value: "", text: "All game types" },
        { value: "educational", text: "Educational" },
        { value: "euro", text: "Euro" },
        { value: "cards", text: "Cards" },
        { value: "rpg", text: "RPG" },
      ],
      minPlayersOptions: [
        { value: "", text: "Any PLayer" },
        { value: "1", text: "1" },
        { value: "2", text: "2" },
        { value: "3", text: "3" },
        { value: "4", text: "4" },
        { value: "5", text: "5" },
      ],
      maxPlayersOptions: [
        { value: "", text: "Any Player" },
        { value: "1", text: "1" },
        { value: "2", text: "2" },
        { value: "3", text: "3" },
        { value: "4", text: "4" },
        { value: "5", text: "5" },
        { value: "6", text: "6" },
        { value: "7", text: "7" },
        { value: "8", text: "8" },
        { value: "9", text: "9" },
        { value: "10", text: "10" },
      ],
      durationOptions: [
        { value: "", text: "Any Duration" },
        { value: 5, text: "5" },
        { value: 10, text: "10" },
        { value: 15, text: "15" },
        { value: 20, text: "20" },
        { value: 25, text: "25" },
        { value: 30, text: "30" },
        { value: 40, text: "40" },
        { value: 50, text: "50" },
        { value: 60, text: "60" },
        { value: 80, text: "80" },
        { value: 100, text: "100" },
        { value: 120, text: "120" },
        { value: 150, text: "150" },
      ],
      AgeOptions: [
        { value: "", text: "Any Age" },
        { value: "+8", text: "+8" },
        { value: "+10", text: "+10" },
        { value: "+12", text: "+12" },
        { value: "+15", text: "+15" },
        { value: "+18", text: "+18" },
      ],
      designerOptions: [],
    };
  },

  methods: {
    loadData(url) {
      this.$api.get(url).then((response) => {
        this.info = response.data.results;
        this.next = response.data.next;
        this.previous = response.data.previous;
      });
    },
    nextPage() {
      this.loadData(this.next);
    },
    previousPage() {
      this.loadData(this.previous);
    },
    magicFilter() {
      this.loadData(
        `/cards/?standard=${this.filters.selectedFormat}` +
          `&hero=${this.filters.selectedHero}` +
          `&card_type=${this.filters.selectedType}` +
          `&quality=${this.filters.selectedQuality}` +
          `&race=${this.filters.selectedRace}` +
          `&expansion=${this.filters.selectedExpansion}` +
          `&cost=${this.filters.selectedCost}` +
          `&page_size=${this.filters.size}`
      );
    },
    resetFilter() {
      Object.entries(this.filters).forEach(([key]) => {
        this.filters[key] = this.savedFilters[key];
      });
      this.searchInfo = null;
    },
    rowClick(row) {
      this.$router.push({
        name: "detail-card",
        params: { cardId: row.id },
      });
    },
  },
  watch: {
    searchInfo() {
      this.loadData("/games/?search=" + this.searchInfo);
    },

    filters: {
      handler() {
        this.magicFilter();
      },
      deep: true,
    },
  },
  mounted() {
    this.loadData("/cards/?page_size=15");
    this.$api.get("/expansions/").then((response) => {
      this.expansionOptions = response.data.results.reduce(
        (options, expansion) => {
          options.push({ value: expansion.id, text: expansion.name });
          return options;
        },
        [{ value: "", text: "All expansions" }]
      );
    });
    this.savedFilters = JSON.parse(JSON.stringify(this.filters));
  },
};
</script>
<style scoped>
</style>