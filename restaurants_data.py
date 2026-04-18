"""Restaurant database for all Saudi cities - sourced from TimeOut, TripAdvisor, Google Maps"""

CITY_RESTAURANTS = {
    'Riyadh': [
        {'name_en': 'Aseeb', 'name_ar': 'عسيب', 'cuisine': 'Saudi Traditional', 'price': 'mid-range'},
        {'name_en': 'Nomas', 'name_ar': 'نوماس', 'cuisine': 'Modern Saudi', 'price': 'luxury'},
        {'name_en': 'Najd Village', 'name_ar': 'القرية النجدية', 'cuisine': 'Najdi', 'price': 'mid-range'},
        {'name_en': 'Fi Glbak', 'name_ar': 'في قلبك', 'cuisine': 'Saudi Home-style', 'price': 'budget'},
        {'name_en': 'Meez', 'name_ar': 'ميز', 'cuisine': 'Multi-regional Saudi', 'price': 'mid-range'},
    ],
    'Jeddah': [
        {'name_en': 'Myazu', 'name_ar': 'ميازو', 'cuisine': 'Japanese', 'price': 'luxury'},
        {'name_en': 'Shababik', 'name_ar': 'شبابيك', 'cuisine': 'Lebanese', 'price': 'mid-range'},
        {'name_en': 'Najd Village', 'name_ar': 'القرية النجدية', 'cuisine': 'Najdi', 'price': 'mid-range'},
        {'name_en': 'AlBaik', 'name_ar': 'البيك', 'cuisine': 'Saudi Fast Food', 'price': 'budget'},
        {'name_en': 'Twina', 'name_ar': 'توينا', 'cuisine': 'Seafood', 'price': 'luxury'},
    ],
    'Aseer': [
        {'name_en': 'Al Salam Palace Revolving', 'name_ar': 'مطعم قصر السلام الدوار', 'cuisine': 'Middle Eastern', 'price': 'mid-range'},
        {'name_en': 'Ali Ramzi Haneeth', 'name_ar': 'حنيذ علي رمزي', 'cuisine': 'Arabic', 'price': 'budget'},
        {'name_en': 'Farfalle', 'name_ar': 'فارفيلي', 'cuisine': 'Italian', 'price': 'mid-range'},
        {'name_en': 'Alkarkand', 'name_ar': 'الكركند', 'cuisine': 'Chinese & Seafood', 'price': 'mid-range'},
        {'name_en': 'Aya Sofia', 'name_ar': 'ايا صوفيا', 'cuisine': 'Turkish', 'price': 'mid-range'},
    ],
    'Madinah': [
        {'name_en': 'Arabesque', 'name_ar': 'أرابيسك', 'cuisine': 'International', 'price': 'mid-range'},
        {'name_en': 'Chef Burak Gurme', 'name_ar': 'شيف بوراك جورميه', 'cuisine': 'Turkish', 'price': 'mid-range'},
        {'name_en': "To'mah", 'name_ar': 'طُعمة', 'cuisine': 'Arabic', 'price': 'mid-range'},
        {'name_en': 'Mahmood Kebab', 'name_ar': 'محمود كباب', 'cuisine': 'Uzbek', 'price': 'mid-range'},
        {'name_en': 'Zaitoon', 'name_ar': 'زيتون', 'cuisine': 'Pakistani & Arabic', 'price': 'mid-range'},
    ],
    'Hail': [
        {'name_en': 'The Coast', 'name_ar': 'ذا كوست', 'cuisine': 'Italian & American', 'price': 'mid-range'},
        {'name_en': 'Al-Marsaai', 'name_ar': 'المرسى', 'cuisine': 'Seafood', 'price': 'mid-range'},
        {'name_en': 'Lamory Cafe', 'name_ar': 'لاموري كافيه', 'cuisine': 'Cafe', 'price': 'budget'},
        {'name_en': 'Marsaai', 'name_ar': 'مرسائي', 'cuisine': 'Italian & Chinese', 'price': 'mid-range'},
        {'name_en': 'Pizza Hut', 'name_ar': 'بيتزا هت', 'cuisine': 'Fast Food', 'price': 'budget'},
    ],
    'Diriyah': [
        {'name_en': 'Aseeb', 'name_ar': 'عسيب', 'cuisine': 'Najdi', 'price': 'luxury'},
        {'name_en': 'Takya', 'name_ar': 'تكية', 'cuisine': 'Modern Saudi', 'price': 'luxury'},
        {'name_en': 'Maiz', 'name_ar': 'ميز', 'cuisine': 'Multi-regional Saudi', 'price': 'luxury'},
        {'name_en': 'Somewhere', 'name_ar': 'سموير', 'cuisine': 'Arabic', 'price': 'mid-range'},
        {'name_en': 'Villa Mamas', 'name_ar': 'فيلا ماماز', 'cuisine': 'Bahraini', 'price': 'mid-range'},
    ],
    'Qassim': [
        {'name_en': 'Al Nakheel', 'name_ar': 'النخيل', 'cuisine': 'International', 'price': 'luxury'},
        {'name_en': 'Taj Mahal', 'name_ar': 'تاج محل', 'cuisine': 'Indian', 'price': 'mid-range'},
        {'name_en': "Grandma's House", 'name_ar': 'بيت الجدة', 'cuisine': 'Middle Eastern', 'price': 'budget'},
        {'name_en': 'Top View', 'name_ar': 'توب فيو', 'cuisine': 'International', 'price': 'mid-range'},
        {'name_en': "Applebee's", 'name_ar': 'ابل بيز', 'cuisine': 'American', 'price': 'mid-range'},
    ],
    'AlUla': [
        {'name_en': 'Harrat', 'name_ar': 'حرة', 'cuisine': 'Middle Eastern', 'price': 'luxury'},
        {'name_en': 'Saffron', 'name_ar': 'زعفران', 'cuisine': 'Thai', 'price': 'mid-range'},
        {'name_en': 'Somewhere AlUla', 'name_ar': 'سموير', 'cuisine': 'Mediterranean', 'price': 'luxury'},
        {'name_en': 'Joontos', 'name_ar': 'خونتس', 'cuisine': 'Spanish', 'price': 'luxury'},
        {'name_en': 'Villa Fayrouz', 'name_ar': 'فيلا فيروز', 'cuisine': 'Lebanese', 'price': 'mid-range'},
    ],
    'Eastern Province': [
        {'name_en': 'Heritage Village', 'name_ar': 'القرية الشعبية', 'cuisine': 'Saudi Traditional', 'price': 'mid-range'},
        {'name_en': 'Beit Misk', 'name_ar': 'بيت مسك', 'cuisine': 'Lebanese', 'price': 'mid-range'},
        {'name_en': 'Fayrouz', 'name_ar': 'فيروز', 'cuisine': 'Lebanese', 'price': 'mid-range'},
        {'name_en': 'Steak House', 'name_ar': 'ستيك هاوس', 'cuisine': 'American', 'price': 'mid-range'},
        {'name_en': "Nando's", 'name_ar': 'ناندوز', 'cuisine': 'Afro-Portuguese', 'price': 'mid-range'},
    ],
    'Taif': [
        {'name_en': 'Bohoo', 'name_ar': 'بووهو', 'cuisine': 'Italian', 'price': 'mid-range'},
        {'name_en': 'Mirag', 'name_ar': 'ميراج', 'cuisine': 'Indian', 'price': 'mid-range'},
        {'name_en': 'Khayal', 'name_ar': 'خيال', 'cuisine': 'Turkish', 'price': 'luxury'},
        {'name_en': 'Hashi Basha', 'name_ar': 'حاشي باشا', 'cuisine': 'Saudi Traditional', 'price': 'mid-range'},
        {'name_en': 'Al Romansiah', 'name_ar': 'الرومانسية', 'cuisine': 'Saudi Traditional', 'price': 'mid-range'},
    ],
    'Al Baha': [
        {'name_en': 'Alnawras Seafood', 'name_ar': 'النورس', 'cuisine': 'Seafood', 'price': 'luxury'},
        {'name_en': 'Karam Misr', 'name_ar': 'كرم مصر', 'cuisine': 'Mediterranean', 'price': 'mid-range'},
        {'name_en': 'Fifth Season', 'name_ar': 'فيفث سيزون', 'cuisine': 'Lebanese & Moroccan', 'price': 'mid-range'},
        {'name_en': 'Pizza Hut', 'name_ar': 'بيتزا هت', 'cuisine': 'Pizza', 'price': 'budget'},
        {'name_en': 'Latino', 'name_ar': 'لاتينو', 'cuisine': 'Mexican & American', 'price': 'luxury'},
    ],
    'Makkah': [
        {'name_en': 'Alqandeel', 'name_ar': 'القنديل', 'cuisine': 'International', 'price': 'luxury'},
        {'name_en': 'Zafaran', 'name_ar': 'زعفران', 'cuisine': 'Mediterranean', 'price': 'luxury'},
        {'name_en': 'Prime', 'name_ar': 'برايم', 'cuisine': 'Healthy', 'price': 'mid-range'},
        {'name_en': 'Al Yasmine', 'name_ar': 'الياسمين', 'cuisine': 'Mediterranean', 'price': 'mid-range'},
        {'name_en': 'Al Rehab', 'name_ar': 'الرحاب', 'cuisine': 'Indian & International', 'price': 'luxury'},
    ],
    'KAEC': [
        {'name_en': 'Steak House', 'name_ar': 'ستيك هاوس', 'cuisine': 'American', 'price': 'mid-range'},
        {'name_en': "Casper & Gambini's", 'name_ar': 'كاسبر آند غامبينيز', 'cuisine': 'International', 'price': 'mid-range'},
        {'name_en': 'Bhar', 'name_ar': 'بهار', 'cuisine': 'Lebanese', 'price': 'mid-range'},
        {'name_en': 'Osmanlizadeler', 'name_ar': 'أوسمانليزاديلير', 'cuisine': 'Turkish', 'price': 'mid-range'},
        {'name_en': 'FireGrill', 'name_ar': 'فاير جريل', 'cuisine': 'Mexican', 'price': 'budget'},
    ],
    'The Red Sea': [
        {'name_en': 'Nyra', 'name_ar': 'نيرا', 'cuisine': 'International', 'price': 'luxury'},
        {'name_en': 'Al Sarab', 'name_ar': 'السراب', 'cuisine': 'Saudi Traditional', 'price': 'luxury'},
        {'name_en': 'Gishiki 45', 'name_ar': 'جيشيكي 45', 'cuisine': 'Japanese', 'price': 'luxury'},
        {'name_en': 'Sita', 'name_ar': 'سيتا', 'cuisine': 'International', 'price': 'luxury'},
        {'name_en': 'Tabrah', 'name_ar': 'طبرة', 'cuisine': 'Seafood', 'price': 'luxury'},
    ],
    'Al Ahsa': [
        {'name_en': 'Flavors', 'name_ar': 'فليفرز', 'cuisine': 'International', 'price': 'luxury'},
        {'name_en': 'Monde', 'name_ar': 'موند', 'cuisine': 'Mediterranean', 'price': 'luxury'},
        {'name_en': 'AlKeet', 'name_ar': 'الكيت', 'cuisine': 'Seafood & Asian', 'price': 'budget'},
        {'name_en': 'Topaz', 'name_ar': 'توباز', 'cuisine': 'Indian & Seafood', 'price': 'mid-range'},
        {'name_en': 'Al Bustan', 'name_ar': 'البستان', 'cuisine': 'Lebanese', 'price': 'mid-range'},
    ],
    'Najran': [
        {'name_en': 'Mashawi Shadi', 'name_ar': 'مشاوي شادي', 'cuisine': 'Turkish', 'price': 'mid-range'},
        {'name_en': 'Sultan Delicious Shawarma', 'name_ar': 'سلطان ديليشز', 'cuisine': 'Arabic', 'price': 'budget'},
        {'name_en': 'Qasr Al-Diyafa', 'name_ar': 'قصر الضيافة', 'cuisine': 'Saudi Traditional', 'price': 'mid-range'},
        {'name_en': 'Al-Bakherah', 'name_ar': 'الباخرة', 'cuisine': 'Seafood', 'price': 'mid-range'},
        {'name_en': 'Makan Indian', 'name_ar': 'مكان الهندي', 'cuisine': 'Indian', 'price': 'mid-range'},
    ],
    'Yanbu': [
        {'name_en': 'Guzel Saray', 'name_ar': 'قوزيل سراي', 'cuisine': 'Mediterranean & Turkish', 'price': 'luxury'},
        {'name_en': 'Jasmine', 'name_ar': 'ياسمين', 'cuisine': 'Italian & Seafood', 'price': 'mid-range'},
        {'name_en': 'Al Marsah Seafood', 'name_ar': 'المرساه', 'cuisine': 'Seafood', 'price': 'luxury'},
        {'name_en': 'Sultan Al Shawaya', 'name_ar': 'سلطان الشواية', 'cuisine': 'Indian & Grill', 'price': 'budget'},
        {'name_en': 'Shangri-La Chinese', 'name_ar': 'شانغريلا', 'cuisine': 'Chinese & Asian', 'price': 'mid-range'},
    ],
    'Al Jubail': [
        {'name_en': 'Brasa De Brazil', 'name_ar': 'براسا دي برازيل', 'cuisine': 'Brazilian', 'price': 'mid-range'},
        {'name_en': 'Taya', 'name_ar': 'طايه', 'cuisine': 'Chinese & Seafood', 'price': 'mid-range'},
        {'name_en': 'Al Tuwayah Buffet', 'name_ar': 'الطوية', 'cuisine': 'International', 'price': 'mid-range'},
        {'name_en': 'Grillo', 'name_ar': 'جريلو', 'cuisine': 'Middle Eastern', 'price': 'mid-range'},
        {'name_en': 'Steak House', 'name_ar': 'ستيك هاوس', 'cuisine': 'American', 'price': 'mid-range'},
    ],
    'Jazan': [
        {'name_en': 'Bandar Aden', 'name_ar': 'بندر عدن', 'cuisine': 'Middle Eastern', 'price': 'luxury'},
        {'name_en': 'Hamora Land', 'name_ar': 'أرض هامور', 'cuisine': 'Seafood', 'price': 'mid-range'},
        {'name_en': 'Loulouat Sahel', 'name_ar': 'لؤلؤة الساحل', 'cuisine': 'Seafood', 'price': 'budget'},
        {'name_en': 'Khana Khazana', 'name_ar': 'خانا خزانا', 'cuisine': 'Indian', 'price': 'mid-range'},
        {'name_en': 'Ocean Basket', 'name_ar': 'أوشن باسكت', 'cuisine': 'African', 'price': 'mid-range'},
    ],
    'Tabuk': [
        {'name_en': 'Western Road Steak & Grill', 'name_ar': 'ويسترن روود', 'cuisine': 'American', 'price': 'luxury'},
        {'name_en': 'Top Grill', 'name_ar': 'قمة المشويات', 'cuisine': 'Middle Eastern', 'price': 'mid-range'},
        {'name_en': 'Syed Al Biryani', 'name_ar': 'سيد البرياني', 'cuisine': 'Indian', 'price': 'mid-range'},
        {'name_en': 'Al Qriah Al Tarithia', 'name_ar': 'القرية التراثية', 'cuisine': 'Middle Eastern', 'price': 'mid-range'},
        {'name_en': 'Taj Mahal', 'name_ar': 'تاج محل', 'cuisine': 'Indian', 'price': 'mid-range'},
    ],
}


def get_restaurant_for_meal(city, meal_type, budget_level='mid-range', used_restaurants=None):
    """Get a restaurant recommendation for a specific city and meal.
    
    Args:
        city: City name
        meal_type: 'lunch' or 'dinner'
        budget_level: 'budget', 'mid-range', or 'luxury'
        used_restaurants: set of already used restaurant names to avoid repeats
    
    Returns:
        dict with restaurant info or None
    """
    import random
    
    if used_restaurants is None:
        used_restaurants = set()
    
    restaurants = CITY_RESTAURANTS.get(city, [])
    if not restaurants:
        # No restaurants for this city - use generic placeholder
        return {'name_en': 'Local Restaurant', 'name_ar': 'مطعم محلي', 'cuisine': 'Local', 'price': 'mid-range'}
    
    # Filter by budget if possible
    budget_map = {
        'budget': ['budget', 'mid-range'],
        'mid-range': ['budget', 'mid-range', 'luxury'],
        'luxury': ['mid-range', 'luxury'],
    }
    allowed_prices = budget_map.get(budget_level, ['budget', 'mid-range', 'luxury'])
    
    # Try to find unused restaurant matching budget
    available = [r for r in restaurants if r['name_en'] not in used_restaurants and r['price'] in allowed_prices]
    
    if not available:
        # Relax: any unused restaurant
        available = [r for r in restaurants if r['name_en'] not in used_restaurants]
    
    if not available:
        # Last resort: any restaurant
        available = restaurants
    
    if available:
        return random.choice(available)
    return None
