def estimate_cost(selected_services, business_scale, creative_scope, content_requirements, is_urgent=False, has_custom_request=False):
    """
    Calculate the estimated cost for a project based on the selected services.

    This module defines the function estimate_cost() which computes a client project's estimated price range based on selected services, business size,
    creative scope, the level of content requirements, urgency, and custom requests.
    """
    # Define base costs for each service
    base_costs = {
        "Brand Strategy Workshop" : (2500, 5000),
        "Logo & Visual Identity Design" : (2000, 7500),
        "Brand Guidelines Document" : (1500, 4000),
        "Website Design & Development" : (5000, 25000),
        "E-commerce Store Development" : (8000, 35000),
        "High-Conversion Landing Page(s)" : (1000, 3500),
        "SEO Strategy" : (2000, 6000),
        "Social Media Management" : (1500, 4000),
        "Professional Copywriting" : (1500, 5000),
        "Photography / Videography" : (2500, 10000)
    }

    # Access services to add low and high totals
    low_total, high_totol = 0, 0
    for service in selected_services:
        if service in base_costs:
            low_total += base_costs[service][0]
            high_totol += base_costs[service][1]

    # Adjust costs based on multipliers
    business_multiplier_map = {
        "Solopreneur" : 0.8,
        "Small Business" : 1.0,
        "Medium Business" : 1.5,
        "Large Enterprise" : 2.0
    }
    business_multiplier = business_multiplier_map.get(business_scale, 1.0) # Fallback default: 1.0

    creative_multiplier_map = {
        "Essential and Functional" : 0.9,
        "Enhanced and Polished" : 1.2,
        "Market-Leading and Comprehensive" : 1.8
    }
    creative_multiplier = creative_multiplier_map.get(creative_scope, 1.0)

    content_multiplier_map = {
        "We provide" : 1.0,
        "Need help" : 1.2,
        "Agency creates" : 1.5
    }
    content_multiplier = content_multiplier_map.get(content_requirements, 1.0)

    # Add up the total cost so far
    low_final = low_total * business_multiplier * creative_multiplier * content_multiplier
    high_final = high_totol * business_multiplier * creative_multiplier * content_multiplier

    # Urgency and Custom Request Multipliers
    if is_urgent:
        low_final *= 1.25
        high_final *= 1.25

    if has_custom_request:
        low_final *= 1.1
        high_final *= 1.4

    return f"{low_final:,.0f}", f"{high_final:,.0f}"

def get_ongoing_retainers(include_seo=False, include_social=False):
    """
    Return a list of ongoing monthly retainers based on selections.
    These are displayed separately from the main project estimate.
    """
    ongoing_services = []

    if include_seo:
        ongoing_services.append({
            "name" : "Ongoing SEO Retainer", 
            "range": "€1,500 - €5,000 / month"})

    if include_social:
        ongoing_services.append({
            "name" : "Social Media & Content Management", 
            "range" : "€2,000 - €7,500 / month"})
        
    return ongoing_services