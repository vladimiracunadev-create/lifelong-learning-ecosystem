// Comprobación opcional con DOM simulado; no sustituye navegador ni revisión visual.
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const root=require('path').resolve(__dirname,'..');
const html=fs.readFileSync(root+'/index.html','utf8');
const elements=new Map();
class Element {
 constructor(id=''){this.id=id;this._html='';this.textContent='';this.value='';this.attributes={};this.listeners={};this.classList={toggle(){return true;}};}
 set innerHTML(v){this._html=v;for(const m of v.matchAll(/\bid="([^"]+)"/g))elements.set(m[1],new Element(m[1]));}
 get innerHTML(){return this._html;}
 addEventListener(k,f){this.listeners[k]=f;}
 setAttribute(k,v){this.attributes[k]=v;}
 getAttribute(k){return this.attributes[k];}
 removeAttribute(k){delete this.attributes[k];}
 focus(){} scrollIntoView(){}
 querySelector(selector){if(selector==='h1'){const m=this._html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/);return m?{textContent:m[1].replace(/<[^>]*>/g,' ')}:null;}return null;}
 querySelectorAll(){return [];}
}
for(const id of ['main-content','main-nav','sidebar-version','footer-version','reading-mode','print-view','portal-data','portal-docs','portal-assets','portal-build'])elements.set(id,new Element(id));
for(const id of ['portal-data','portal-docs','portal-assets','portal-build'])elements.get(id).textContent=html.match(new RegExp('<script id="'+id+'" type="application/json">([\\s\\S]*?)<\\/script>'))[1];
const document={getElementById(id){const el=elements.get(id);if(!el)throw new Error('Missing element '+id);return el;},querySelectorAll(){return [];},addEventListener(){},documentElement:new Element('html')};
const sandbox={document,location:{hash:''},window:{addEventListener(){},scrollTo(){},print(){}},requestAnimationFrame(f){f();},URL,URLSearchParams,console,Event:class{},Set,Map};
const context=vm.createContext(sandbox);vm.runInContext(html.match(/<script>\s*([\s\S]*?)<\/script>/)[1],context,{timeout:2000});
function check(expression){return vm.runInContext(expression,context,{timeout:2000});}
const errors=[],main=elements.get('main-content');
let details=0,docs=0;
for(const section of ['inicio','mallas','programas','competencias','apoyos','evaluacion','documentos']){sandbox.location.hash='#'+section;check('renderRoute()');assert(main.innerHTML.includes('<h1'),section+' heading');assert(!main.innerHTML.includes('[object Object]'),section+' object leak');}
const maps=check('Object.fromEntries(Object.entries(MAP).map(([k,v])=>[k,Object.keys(v)]))');
for(const [kind,ids] of Object.entries(maps))for(const id of ids){sandbox.location.hash='#'+kind+'/'+id;check('renderRoute()');assert(!main.innerHTML.includes('undefined'),id+' undefined');assert(!main.innerHTML.includes('[object Object]'),id+' object leak');assert(main.innerHTML.includes(id),id+' rendered');details++;}
for(const path of check('Object.keys(DOCS)')){sandbox.location.hash='#doc/'+encodeURIComponent(path);check('renderRoute()');assert(main.innerHTML.includes('class="markdown"'),path+' rendered');assert(!main.innerHTML.includes('<script'),path+' unsafe HTML');docs++;}
sandbox.location.hash='#inicio';check('renderRoute()');assert(main.innerHTML.includes('30 flujos nativos'));assert(main.innerHTML.includes('Software y computación'));assert(main.innerHTML.includes('hero-visual'));
const hostile=check("inlineMarkdown('<script>alert(1)</script> [clic](javascript:alert(1)) ![imagen](https://example.com/image.png)', 'README.md')");assert(!hostile.includes('<script'));assert(!hostile.includes('href="javascript:'));assert(!hostile.includes('<img'));
const localImage=check("inlineMarkdown('![Mapa](docs/assets/campus-federado.svg)', 'README.md')");assert(localImage.includes('<img'));assert(localImage.includes('data:image/svg+xml;base64,'));
const list=check("renderMarkdown('# Prueba\\n\\n- Uno\\n  - Dos\\n- Tres\\n\\n| A | B |\\n| --- | --- |\\n| C | D |', 'README.md').html");assert(list.includes('<table>'));assert(list.includes('<ul>'));
console.log(JSON.stringify({method:'Controlled DOM stubs in Node vm; not a browser or visual QA',sections:7,detail_views:details,documents:docs,campus:'OK',local_svg:'OK',safe_markdown:'OK',markdown_table_and_lists:'OK'}));
