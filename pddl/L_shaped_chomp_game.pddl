(define (domain L_shaped_chomp_game)
    (:objects ?v1 ?v2)
    (:type normal)
    (:tercondition (and (= ?v1 1) (= ?v2 1)))
    (:constraint (and (>= ?v1 1) (>= ?v2 1)))
    (:action eat1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 1))
        :effect (assign ?v1 (- ?k 1)))
    (:action eat2
        :parameters (?k)
        :precondition (and (>= ?v2 ?k) (> ?k 1))
        :effect (assign ?v2 (- ?k 1)))
 