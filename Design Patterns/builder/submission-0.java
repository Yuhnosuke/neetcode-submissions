class Meal {

    private double cost;
    private boolean takeOut;
    private String main;
    private String drink;

    double getCost() {
        return this.cost;
    }

    boolean getTakeOut() {
        return this.takeOut;
    }

    String getMain() {
        return this.main;
    }

    String getDrink() {
        return this.drink;
    }

    void setCost(double cost) {
        this.cost = cost;
    }

    void setTakeOut(boolean takeOut) {
        this.takeOut = takeOut;
    }

    void setMain(String main) {
        this.main = main;
    }

    void setDrink(String drink) {
        this.drink = drink;
    }
}

interface Builder {
    MealBuilder addCost(double cost);
    MealBuilder addTakeOut(boolean takeOut);
    MealBuilder addMainCourse(String main);
    MealBuilder addDrink(String drink);
}

class MealBuilder implements Builder {
    private Meal meal;

    public MealBuilder() {
        this.meal = new Meal();
    }

    @Override
    public MealBuilder addCost(double cost) {
        meal.setCost(cost);
        return this;
    }

    @Override
    public MealBuilder addTakeOut(boolean takeOut) {
        meal.setTakeOut(takeOut);
        return this;
    }

    @Override
    public MealBuilder addMainCourse(String main) {
        meal.setMain(main);
        return this;
    }

    @Override
    public MealBuilder addDrink(String drink) {
        meal.setDrink(drink);
        return this;
    }

    Meal build() {
        return this.meal;
    }
}
