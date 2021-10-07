(define (domain welter)
	(:objects ?v1 ?v2)
	(:tercondition (or (and (= ?v1 0) (= ?v2 1)) (and (= ?v1 1) (= ?v2 0)) ))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (!= ?v1 ?v2)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 0) (!= (- ?v1 ?k) ?v2))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (>= ?v2 ?k) (> ?k 0) (!= (- ?v2 ?k) ?v1))
        :effect (assign ?v2 (- ?v2 ?k)))
)