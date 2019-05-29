----------------------------------------------------------------------
--CHALLENGE 1
----------------------------------------------------------------------
----------------------------------------------------------------------
--STEP 1
----------------------------------------------------------------------
create temporary table Royalties
SELECT
	ta.title_id title_id,
    	ta.au_id au_id,
    	t.price*s.qty*(t.royalty/100)*(ta.royaltyper/100) Profit
    
FROM 
	sales s
    JOIN
	titles t
    	on
	s.title_id=t.title_id
    JOIN
	titleauthor ta
    	on
	ta.title_id=t.title_id
    join 
	authors a 
    on ta.au_id=a.au_id
;
----------------------------------------------------------------------
--STEP 2 
----------------------------------------------------------------------

create temporary table ProffitByAuthor
SELECT
	title_id,
	au_id,
	sum(Profit) Profit
	
FROM
	Royalties
GROUP BY
        au_id,title_id;

----------------------------------------------------------------------
--STEP 3 
----------------------------------------------------------------------

SELECT
	p.title_id title_id,
	p.au_id au_id,
	Profit + t.advance Profit
FROM
	ProffitByAuthor p
JOIN
	titles t
	ON
	t.title_id=p.title_id
order by profit desc
LIMIT 3
;

----------------------------------------------------------------------
--CHALLENGE 2
----------------------------------------------------------------------


SELECT
	profitByAuthor.title_id title_id,
	profitByAuthor.au_id au_id,
	Profit + t.advance Profit
FROM
	(SELECT
		title_id,
		au_id,
		sum(royalties.Profit) Profit
	
	FROM
		(SELECT
			ta.title_id title_id,
    			ta.au_id au_id,
    			t.price*s.qty*(t.royalty/100)*(ta.royaltyper/100) Profit
    
		FROM 
			sales s
    		JOIN
			titles t
    		on
			s.title_id=t.title_id
    		JOIN
			titleauthor ta
    			on
			ta.title_id=t.title_id
    		join 
			authors a 
    			on
			ta.au_id=a.au_id
		)royalties

	GROUP BY
                au_id,title_id
	)profitByAuthor

JOIN
	titles t
	ON
	t.title_id=profitByAuthor.title_id
order by profit desc
LIMIT 3
;


