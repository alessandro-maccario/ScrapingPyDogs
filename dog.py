class Dog:

    """
        Dog class to instanciate and set all the Dogs' attributes
        to be taken from the webpage.
        It contains:
        - BASIC FIELDS;
        - ADAPTABILITY FIELDS;
        - ALL AROUND FRIENDLINESS FIELDS;
        - HEALTH AND GROOMING NEEDS FIELDS;
        - TRAINABILITY FIELDS;
        - PHYSICAL NEEDS FIELDS;
        - VITAL STATS FIELDS.
    """

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance

    # SET BASIC FIELDS
    def set_description(self, description):
        self.description = description

    def set_image(self, image):
        self.image = image

    # SET ADAPTABILITY FIELDS
    def set_adapts_well_to_apartment_living(self, adapts_well_to_apartment_living):
        self.adapts_well_to_apartment_living = adapts_well_to_apartment_living

    def set_good_for_novice_owners(self, good_for_novice_owners):
        self.good_for_novice_owners = good_for_novice_owners

    def set_sensitivity_level(self, sensitivity_level):
        self.sensitivity_level = sensitivity_level

    def set_tolerates_being_alone(self, tolerates_being_alone):
        self.tolerates_being_alone = tolerates_being_alone

    def set_tolerates_cold_weather(self, tolerates_cold_weather):
        self.tolerates_cold_weather = tolerates_cold_weather

    def set_tolerates_hot_weather(self, tolerates_hot_weather):
        self.tolerates_hot_weather = tolerates_hot_weather

    # SET ALL AROUND FRIENDLINESS FIELDS
    def set_affectionate_with_family(self, affectionate_with_family):
        self.affectionate_with_family = affectionate_with_family

    def set_kid_friendly(self, kid_friendly):
        self.kid_friendly = kid_friendly

    def set_dog_friendly(self, dog_friendly):
        self.dog_friendly = dog_friendly

    def set_friendly_toward_strangers(self, friendly_toward_strangers):
        self.friendly_toward_strangers = friendly_toward_strangers

    # SET HEALTH AND GROOMING NEEDS FIELDS
    def set_amount_of_shedding(self, amount_of_shedding):
        self.amount_of_shedding = amount_of_shedding

    def set_drooling_potential(self, drooling_potential):
        self.drooling_potential = drooling_potential

    def set_easy_to_groom(self, easy_to_groom):
        self.easy_to_groom = easy_to_groom

    def set_general_health(self, general_health):
        self.general_health = general_health

    def set_potential_for_weight_gain(self, potential_for_weight_gain):
        self.potential_for_weight_gain = potential_for_weight_gain

    def set_size(self, size):
        self.size = size

    # SET TRAINABILITY FIELDS
    def set_easy_to_train(self, easy_to_train):
        self.easy_to_train = easy_to_train

    def set_intelligence(self, intelligence):
        self.intelligence = intelligence

    def set_potential_for_mouthiness(self, potential_for_mouthiness):
        self.potential_for_mouthiness = potential_for_mouthiness

    def set_prey_drive(self, prey_drive):
        self.prey_drive = prey_drive

    def set_tendency_to_bark_or_howl(self, tendency_to_bark_or_howl):
        self.tendency_to_bark_or_howl = tendency_to_bark_or_howl

    def set_wanderlust_potential(self, wanderlust_potential):
        self.wanderlust_potential = wanderlust_potential

    # SET PHYSICAL NEEDS FIELDS
    def set_energy_level(self, energy_level):
        self.energy_level = energy_level

    def set_intensity(self, intensity):
        self.intensity = intensity

    def set_exercise_needs(self, exercise_needs):
        self.exercise_needs = exercise_needs

    def set_potential_for_playfulness(self, potential_for_playfulness):
        self.potential_for_playfulness = potential_for_playfulness

    # SET VITAL STATS FIELDS
    def set_dog_breed_group(self, dog_breed_group):
        self.dog_breed_group = dog_breed_group

    def set_height(self, height):
        self.height = height

    def set_weight(self, weight):
        self.weight = weight

    def set_life_span(self, life_span):
        self.life_span = life_span