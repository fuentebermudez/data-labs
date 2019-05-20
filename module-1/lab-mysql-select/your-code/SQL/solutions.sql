----------------------------------------------------------------------
--CHALLENGE 1
----------------------------------------------------------------------
SELECT
    authors.au_id as AUTHOR_ID,
    au_lname as LAST_NAME,
    au_fname as FIRST_NAME,
    titles.title as TITLE,
    publishers.pub_name as PUBLISHER
    FROM 
    authors 
    JOIN 
		titleauthor on authors.au_id=titleauthor.au_id 
    JOIN 
		titles on titles.title_id=titleauthor.title_id 
    JOIN 
		publishers on publishers.pub_id=titles.pub_id;

----------------------------------------------------------------------
--CHALLENGE 2
----------------------------------------------------------------------

SELECT
	authors.au_id as AUTHOR_ID,
    au_lname as LAST_NAME,
    au_fname as FIRST_NAME,
    publishers.pub_name as PUBLISHER,
    count(*) as TITLE_COUNT
    FROM 
    authors 
    JOIN 
		titleauthor on authors.au_id=titleauthor.au_id 
    JOIN 
		titles on titles.title_id=titleauthor.title_id 
    JOIN 
		publishers on publishers.pub_id=titles.pub_id
        
	GROUP BY
		authors.au_id,publishers.pub_name;

----------------------------------------------------------------------
--CHALLENGE 3
----------------------------------------------------------------------


SELECT
	authors.au_id as AUTHOR_ID,
    au_lname as LAST_NAME,
    au_fname as FIRST_NAME,
    sum(titles.ytd_sales) TOTAL
    
    FROM 
    authors 
    JOIN 
		titleauthor on authors.au_id=titleauthor.au_id 
    JOIN 
		titles on titles.title_id=titleauthor.title_id 
        
	GROUP BY
		authors.au_id
    ORDER BY sum(titles.ytd_sales) DESC limit 3;

----------------------------------------------------------------------
--CHALLENGE 4
----------------------------------------------------------------------

SELECT
	authors.au_id as AUTHOR_ID,
    au_lname as LAST_NAME,
    au_fname as FIRST_NAME,
    case when 
    sum(titles.ytd_sales) IS NULL then 0 else sum(titles.ytd_sales) END TOTAL
    
    FROM 
    authors 
    left JOIN 
		titleauthor on authors.au_id=titleauthor.au_id 
    left JOIN 
		titles on titles.title_id=titleauthor.title_id 
        
	GROUP BY
		authors.au_id
    ORDER BY sum(titles.ytd_sales) DESC ;

----------------------------------------------------------------------
--BONUS CHALLENGE
----------------------------------------------------------------------



SELECT
	authors.au_id as AUTHOR_ID,
   	au_lname as LAST_NAME,
    	au_fname as FIRST_NAME,
    	(sum(titles.royalty)*(titleauthor.royaltyper/100)) + sum(titles.advance) as PROFIT --Entiendo que royaltyper es un porcentaje del total del royalty
    
    FROM 
    authors 
    JOIN 
		titleauthor on authors.au_id=titleauthor.au_id 
    JOIN 
		titles on titles.title_id=titleauthor.title_id 
        
	GROUP BY
		authors.au_id
ORDER BY sum(titles.ytd_sales) DESC limit 3;
